from fastapi import FastAPI, WebSocket, HTTPException, status
from starlette.websockets import WebSocketDisconnect
from app.schema import IdUser, UserFriends
from app.manager import manager
import json

app = FastAPI()


@app.post("/post/feed/posted")
async def push_notify_post(user_id: str):
    await manager.send_message(user_id)
    return {"message": "Notification sent to WebSocket clients"}


@app.post("/set-user-friends")
async def set_user_friends(user_friends: UserFriends):
    try:
        await manager.set_user_friends(user_friends.id, user_friends.user_friends)
        return {f"Set user friends {user_friends.id}": "ok"}
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User friends not set"
        )


@app.post("/get-user-friends")
async def get_user_friends(id_user: IdUser):
    try:
        result = await manager.get_user_friends(id_user.id)
        if result:
            return result
        else:
            return {"User not exist"}
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not set"
        )


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            id_user = json.loads(data)
            print(id_user["id_user"])

    except WebSocketDisconnect:
        manager.disconnect(websocket)
