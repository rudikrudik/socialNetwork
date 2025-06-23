import redis
import json
from app.db.db_query import raw_query
from app.config import settings

key_post = [*raw_query("SELECT * FROM user_posts WHERE id = 42"), True]


def redis_connect() -> redis:
    r_connect = redis.Redis(host=settings.REDIS_CACHE_HOST,
                            port=settings.REDIS_CACHE_PORT,
                            db=settings.REDIS_DB,
                            password=settings.REDIS_PASSWORD
                            )
    try:
        r_connect.ping()
    except redis.exceptions.RedisError as error:
        print(f"Error {error}")

    return r_connect


def redis_db_proxy_get_query_key(id_post: int) -> tuple:
    r = redis_connect()
    return r.get(str(id_post)) if r.exists(str(id_post)) else None


def redis_db_proxy_set_query_key(id_post, result_from_sql: tuple) -> None:
    dict_str = json.dumps(result_from_sql, indent=4, sort_keys=True, default=str)
    r.hset(str(id_post), dict_str)
