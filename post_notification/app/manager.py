import json
from starlette.websockets import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_user_connections: dict = {}

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        data = await websocket.receive_text()
        id_user = json.loads(data)

        self.active_user_connections[int(id_user["id_user"])] = websocket
        for i in self.active_user_connections:
            print(f"Active Connections: {i}", flush=True)

    async def disconnect(self, websocket: WebSocket):
        data = await websocket.receive_text()
        id_user = json.loads(data)
        del self.active_user_connections[id_user["id_user"]]

    async def send_message(self, user_id, friends):
        for friend in friends:
            print(f"Type friend: {friend}")
            if friend in self.active_user_connections.keys():
                await self.active_user_connections[friend].send_text(f"New post from {user_id}")
            else:
                print(f"{friend} not in active connection")


manager = ConnectionManager()
