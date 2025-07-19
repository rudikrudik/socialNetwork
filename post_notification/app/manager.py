from typing import Any
import json
from starlette.websockets import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_user_connections: dict = {}
        self.user_friends: dict = {}

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        data = await websocket.receive_text()
        id_user = json.loads(data)

        self.active_user_connections[id_user["id_user"]] = websocket
        for i in self.active_user_connections:
            print(f"Active Connections: {i}", flush=True)

    async def disconnect(self, websocket: WebSocket):
        data = await websocket.receive_text()
        id_user = json.loads(data)
        del self.active_user_connections[id_user["id_user"]]

    async def send_message(self, message: str):
        print(f"get message: {message}", flush=True)

        for connection in self.active_user_connections:
            await connection.send_text(message)

    async def get_user_friends(self, user_id: int) -> list | None:
        try:
            return self.user_friends[user_id]
        except KeyError as error:
            return None

    async def set_user_friends(self, user_id: int, user_friends: list) -> bool:
        try:
            self.user_friends[user_id] = user_friends
            return True
        except KeyError as error:
            return False


manager = ConnectionManager()
