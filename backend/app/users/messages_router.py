from fastapi import APIRouter, HTTPException, Depends, status
from app.users.schema import UserMessage
from app.mongo_db import mongo_db
from app.users import dependencies as dep


router = APIRouter()


@router.post("/dialog/{from_user}/send/{to_user}")
def send_message_to_user(from_user: int, to_user: int, user_message: UserMessage):
    # token: str = Depends(dep.get_token)
    # user_id_from_token = dep.get_current_user(token)

    try:
        result = mongo_db.mongodb_insert_one(from_user, to_user, user_message.message)
        if result:
            return {"Message send": "ok", "from": from_user, "to": to_user}
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
        result_query = []
        for r in mongo_db.mongodb_query(user_id):
            result_query.append(r)
        return result_query
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Post can Create"
        )
