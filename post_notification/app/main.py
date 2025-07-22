from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect
from app.schema import UserFriends
from app.manager import manager

app = FastAPI()


@app.post("/post/feed/posted")
async def push_notify_post(data: UserFriends):
    await manager.send_message(data.id, data.friends)
    return {"message": "Notification sent to WebSocket clients"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        await manager.disconnect(websocket)
