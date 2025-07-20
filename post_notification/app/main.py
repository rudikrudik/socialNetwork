from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect
from app.schema import UserFriends
from app.manager import manager
import json

app = FastAPI()


@app.post("/post/feed/posted")
async def push_notify_post(data: UserFriends):
    print("/post/feed/posted data:", data.id, data.friends, flush=True)
    await manager.send_message(data)
    return {"message": "Notification sent to WebSocket clients"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            id_user = json.loads(data)
            print(id_user, flush=True)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
