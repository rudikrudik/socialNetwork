from fastapi import APIRouter, HTTPException, Depends, status
from app.users.schema import UserMessage
from app.mongo_db import mongo_db
from app.users import dependencies as dep


router = APIRouter()


@router.post("/dialog/{user_id}/send")
def send_message_to_user(user_id: int, user_message: UserMessage, token: str = Depends(dep.get_token)):
    user_id_from_token = dep.get_current_user(token)

    try:
        return mongo_db.mongodb_insert_one(user_id_from_token, user_id, user_message.message)
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Posts not found"
        )


@router.get("/dialog/{user_id}/list")
def get_all_messages_from_user(user_id: int, token: str = Depends(dep.get_token)):
    try:
        return mongo_db.mongodb_query(user_id)
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Post can Create"
        )
