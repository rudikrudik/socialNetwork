from app.config import settings
from app.db.db_query import raw_query
from app.redis_cache.redis_db import redis_db_proxy_get_query_key, redis_db_proxy_set_query_key, redis_db_proxy_delete_key


def get_user_posts(id: int):
    return raw_query(f"SELECT * FROM user_posts WHERE user_id = '{id}'", False)


def delete_user_post(id_user: int, id_post: int):
    redis_db_proxy_delete_key(id_post)

    return raw_query(f"DELETE FROM user_posts WHERE user_id = '{id_user}' AND id = '{id_post}' ",
                     True, settings.DB_PORT_WRITE)


def create_user_post(id_post: int, post_content: str):
    return raw_query(f"INSERT INTO user_posts (user_id, post_date_create, post_content) VALUES ({id_post},"
                     f"date_trunc('second', now()::timestamp), '{post_content}');",
                     True, settings.DB_PORT_WRITE)


def update_user_post(id_post: int, post_content: str):
    # Delete not edited post from cache
    redis_db_proxy_delete_key(id_post)

    return raw_query(f"UPDATE user_posts SET post_content = '{post_content}' WHERE id = {id_post}",
                     True, settings.DB_PORT_WRITE)


def get_user_post_by_id(id_post: int) -> tuple:
    # with redis cache
    result_from_redis = redis_db_proxy_get_query_key(id_post)
    if result_from_redis:
        return result_from_redis
    else:
        result_from_sql = raw_query(f"SELECT * FROM user_posts WHERE id = {id_post}", True)
        if result_from_sql is not None:
            redis_db_proxy_set_query_key(id_post, result_from_sql)
        return result_from_sql


def get_post_limit_and_offset(user_id: int, posts_limit: int, offset: int):
    return raw_query(f"SELECT * FROM user_posts WHERE user_id IN"
                     f"(SELECT friend_id FROM user_friends WHERE user_id = {user_id})"
                     f"ORDER BY post_date_create DESC"
                     f"LIMIT {posts_limit} OFFSET {offset}", False)
