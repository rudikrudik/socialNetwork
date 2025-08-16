from fastapi import APIRouter, HTTPException, Depends, status
from app.users.schema import UserMessage
from app.redis_dialogs import redis_dialogs as redis_db

# temporary not used
# from app.mongo_db import mongo_db
# from app.users import dependencies as dep

router = APIRouter()


@router.post("/dialog/{from_user}/send/{to_user}")
def send_message_to_user(from_user: int, to_user: int, user_message: UserMessage):
    # token: str = Depends(dep.get_token)
    # user_id_from_token = dep.get_current_user(token)

    try:
        # dialog in mongo DB
        #result = mongo_db.mongodb_insert_one(from_user, to_user, user_message.message)

        # dialog in redis DB
        result = redis_db.redis_db_send_message_from_to(from_user, to_user, user_message.message)
        if result:
            return {"Message send": "ok", "from": from_user, "to": to_user}
        else:
            return {"Message send": "false"}
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User message not send"
        )


@router.post("/dialog/{from_user}/get/{to_user}")
def get_messages_from_to_user(from_user: int, to_user: int):
    # token: str = Depends(dep.get_token)
    # user_id_from_token = dep.get_current_user(token)

    try:
        result = redis_db.redis_db_get_user_messages(from_user, to_user)
        if result:
            return result
        else:
            return {"Message get": "false"}
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User dialog not found"
        )


@router.get("/dialog/{user_id}/list")
def get_all_messages_from_user(user_id: int):
    try:
        result_query = []
        for r in redis_db.redis_search_user_dialog(user_id):
            result_query.append(r)
        return result_query
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dialog not find"
        )
