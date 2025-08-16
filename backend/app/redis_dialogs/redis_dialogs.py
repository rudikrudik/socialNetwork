import json
import redis

from datetime import datetime
from app.config import settings


def redis_connect():
    r_connect = redis.Redis(host=settings.REDIS_DIALOG_HOST,
                            port=settings.REDIS_DIALOG_PORT,
                            db=settings.REDIS_DIALOG_DB,
                            password=settings.REDIS_DIALOG_PASSWORD
                            )
    try:
        r_connect.ping()
    except redis.exceptions.RedisError as error:
        print(f"Error {error}")

    return r_connect


def find_sort_id(from_user: int, to_user: int) -> tuple:
    return from_user if from_user < to_user else to_user, to_user if to_user > from_user else from_user


def redis_db_send_message_from_to(from_user: int, to_user: int, message: str) -> None:
    r = redis_connect()
    first, last = find_sort_id(from_user, to_user)

    data = {
        "from_user": from_user,
        "to_user": to_user,
        "date": datetime.now().strftime("%Y-%M-%d %H:%m:%S"),
        "message": message
    }

    r.rpush(f"dialog:{first}:{last}", json.dumps(data, ensure_ascii=False))


def redis_search_user_dialog(id_user: int) -> list | None:
    r = redis_connect()
    list_names = []

    for key in r.scan_iter(f"dialog:{id_user}:*"):
        list_names.append(key)

    if list_names:
        return list_names
    else:
        for key in r.scan_iter(f"dialog:*:{id_user}"):
            list_names.append(key)

    return list_names if list_names else None


def redis_db_get_user_messages(from_user: int, to_user: int) -> list:
    r = redis_connect()
    first, last = find_sort_id(from_user, to_user)
    dialog = r.lrange(f"dialog:{first}:{last}", 0, -1)

    return [json.loads(i.decode('utf-8')) for i in dialog]
