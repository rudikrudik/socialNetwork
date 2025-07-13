from typing import Any, Mapping
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError, OperationFailure
from datetime import datetime
from pymongo.synchronous.collection import Collection
from app.config import settings
from bson import json_util
import json


def mongodb_connect() -> Collection[Mapping[str, Any] | Any]:
    try:
        client = MongoClient(f"mongodb://{settings.MONGODB_HOST}:{settings.MONGODB_PORT}/")
        db = client[f"{settings.MONGODB_DB}"]
        return db[f"{settings.MONGODB_COLLECTIONS}"]
    except ServerSelectionTimeoutError as error:
        print(f"MongoDB Connection error: {error}")

    except ConnectionFailure as error:
        print(f"Connection error {error}")


def mongodb_insert_one(id_from: int, to_id: int, content: str) -> str:
    message = {"id_from": id_from,
               "to_id": to_id,
               "date": datetime.now(),
               "content": content}
    try:
        return mongodb_connect().insert_one(message).inserted_id
    except OperationFailure as error:
        print(f"Insert error {error}")


def mongodb_query(id_from: int) -> list:
    try:
        return json.loads(json_util.dumps(mongodb_connect().find({"id_from": id_from})))
    except OperationFailure as error:
        print(f"Query error {error}")
