from fastapi import APIRouter, HTTPException, Depends, status
from app.users.schema import UserMessage
from app.mongo_db import mongo_db
from app.users import dependencies as dep


router = APIRouter()


@router.post("/dialog/{user_id}/send")
def send_message_to_user(user_id: int, user_message: UserMessage):
    # token: str = Depends(dep.get_token)
    # user_id_from_token = dep.get_current_user(token)

    try:
        result = mongo_db.mongodb_insert_one(1, user_id, user_message.message)
        if result:
            return {"Message send": "ok", "from": 1, "to": user_id}
        else:
            return {"Message send": "false"}
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Posts not found"
        )


@router.get("/dialog/{user_id}/list")
def get_all_messages_from_user(user_id: int):
    try:
        return list(mongo_db.mongodb_query(user_id))
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Post can Create"
        )
