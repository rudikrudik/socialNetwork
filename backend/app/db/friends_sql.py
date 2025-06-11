from app.config import settings
from app.db.db_query import raw_query


def get_user_friends(id: int):
    return raw_query(f"SELECT * FROM user_posts WHERE user_id = '{id}'", False)

