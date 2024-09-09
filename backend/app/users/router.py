from fastapi import APIRouter, HTTPException, Response, Depends, status
from app.users.schema import User, CreateUser, AuthUser
from app.db import user as db_user
from app.users import auth
from app.users import dependencies as dep


router = APIRouter()


@router.get(
    "/user/get/{id}",
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
def get_user(id: int) -> User:
    result = db_user.get_user_by_id(id)
    if result is None:
        raise HTTPException(status_code=404, detail=f"User with id: {id} does not exist")
    return {"id": result[0],
            "first_name": result[1],
            "last_name": result[2],
            "birthday": result[3],
            "gender": result[4],
            "hobby": result[5],
            "city": result[6]}


@router.post(
    "/user/register",
    description="Регистрация нового пользователя",
    responses={
        400: {"description": "Невалидные данные"},
        200: {
            "content": {"application/json": {}},
            "description": "Успешная регистрация",
        }
    },
)
def register_user(item: CreateUser):
    if db_user.find_user_by_login(item.login) is not None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User already exists")
    db_user.create_user(item.first_name, item.last_name, item.birthday,
                        item.gender, item.hobby, item.city, item.login, item.password)
    return {"Message": "User successfully registered"}


@router.post("/login")
def login_user(response: Response, user_data: AuthUser):
    result = db_user.auth_user(user_data.login)
    if result is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Wrong username or password")

    if not auth.verify_password(user_data.password, result[2]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Wrong your username or password")

    access_token = auth.create_access_token({"sub": str(result[0])})
    response.set_cookie(key="user_access_token", value=access_token, httponly=True)
    return {"access_token": access_token, "refresh_token": None}


@router.post("/logout")
def logout_user(response: Response):
    response.delete_cookie(key="user_access_token")
    return {"Message": "User logout"}


@router.get("/user/all")
def get_all_users(token: str = Depends(dep.get_token)):
    return db_user.get_all_users()


@router.get("/check")
def health_check():
    return {"Message": "ok"}
