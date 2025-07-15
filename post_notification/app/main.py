from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect

from app.manager import manager


app = FastAPI()


@app.post("/send-message")
async def push_product():
    await manager.send_message("New product available!")
    return {"message": "Message sent to WebSocket clients"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        manager.disconnect(websocket)
