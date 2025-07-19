from fastapi import FastAPI, WebSocket, HTTPException, status
from starlette.websockets import WebSocketDisconnect
from app.schema import IdUser, UserFriends
from app.manager import manager
import json

app = FastAPI()


@app.post("/send-message")
async def push_notify_post(data: str):
    await manager.send_message(f"New product available! {data}")
    return {"message": "Message sent to WebSocket clients"}


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
    return await manager.get_user_friends(id_user.id)


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
