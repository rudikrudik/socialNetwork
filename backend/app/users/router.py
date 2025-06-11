from fastapi import APIRouter, HTTPException, Response, Depends, status
from fastapi.responses import FileResponse
from app.users.schema import User, CreateUser, AuthUser, RegisterNewUser, SearchUser, IdUser, CreateUserPost, UpdateUserPost, IdPost
from app.db import user as db_user
from app.users import auth
from app.users import dependencies as dep


router = APIRouter()
favicon_path = 'favicon.ico'


# Route to favicons
@router.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

@router.get(
    "/user/get/",
    description="Получение анкеты пользователя",
    response_model=User,
    responses={
        400: {"description": "Невалидные данные"},
        404: {"description": "Анкета не найдена"},
        422: {"description": "Ошибка валидации"},
        500: {},
        503: {},
        200: {
            "content": {"application/json": {}},
            "description": "Успешное получение анкеты пользователя",
        }
    },
)
def get_user(id_user: IdUser) -> User:
    result = db_user.get_user_by_id(id_user.id)

    if result is None:
        raise HTTPException(status_code=404, detail=f"User with id: {id_user.id} does not exist")
    return {"id": result[0],
            "first_name": result[1],
            "last_name": result[2],
            "birthday": result[3],
            "gender": result[4],
            "hobby": result[5],
            "city": result[6]}


@router.post("/user/register",
             description="Регистрация нового пользователя",
             responses={
                400: {"description": "Невалидные данные"},
                200: {
                    "content": {"application/json": {}},
                    "description": "Успешная регистрация",
                        }
                })
def register_user(register_new_user: RegisterNewUser):
    if db_user.find_user_by_login(register_new_user.login) is not None:
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail="User already exists")
    result = db_user.create_user(
                                register_new_user.first_name,
                                register_new_user.last_name,
                                register_new_user.login,
                                register_new_user.password
                                )
    return {"user id": f"{result[0]}"}


@router.post("/login")
def login_user(response: Response, login_item: AuthUser):
    result = db_user.auth_user(login_item.login)

    if result is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Wrong username or password")

    if not auth.verify_password(login_item.password, result[2]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Wrong your username or password")

    access_token = auth.create_access_token({"sub": str(result[0])})
    response.set_cookie(key="user_access_token", value=access_token, httponly=True)
    return {"token": access_token}


@router.post("/logout")
def logout_user(response: Response):
    response.delete_cookie(key="user_access_token")
    return {"Message": "User logout"}


@router.get("/user/all")
def get_all_users(token: str = Depends(dep.get_token)):
    return db_user.get_all_users()


@router.get("/user/search")
def search_users(search_user: SearchUser):
    if search_user.first_name.isalpha() and search_user.last_name.isalpha():
        result = db_user.search_users(search_user.first_name, search_user.last_name)

        if result:
            return result
        else:
            return {"Message": "Nothing found"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Error data request")


@router.get("/check")
def health_check():
    try:
        result = db_user.get_user_by_id(1)
        return {"Message": f"{result[0]}"}
    except BaseException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Error connect to database")


