from app.config import settings
from app.db.db_query import raw_query


def get_user_friends(id: int):
    return raw_query(f"SELECT * FROM user_friends WHERE user_id = '{id}'", False)


def add_user_friend(user_id: int, friend_id: int):
    return raw_query(f"INSERT INTO user_friends (user_id, friend_id) VALUES ({user_id}, {friend_id}) "
                     f"RETURNING friend_id;",
                     True, settings.DB_PORT_WRITE)


def delete_user_friend(user_id: int, friend_id: int):
    return raw_query(f"DELETE FROM user_friends WHERE user_id = {user_id} and friend_id = {friend_id}"
                     f" RETURNING friend_id;", True, settings.DB_PORT_WRITE)
