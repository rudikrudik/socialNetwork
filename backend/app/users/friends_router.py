from fastapi import APIRouter, HTTPException, Response, Depends, status
from app.users.schema import User
from app.db import friends_sql as db_friends
from app.users import auth
from app.users import dependencies as dep


router = APIRouter()


@router.get("/user/friends")
def get_user_friends(token: str = Depends(dep.get_token)):
    user_id = dep.get_current_user(token)

    try:
        return db_friends.get_user_friends(user_id)
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Friends not found"
        )


