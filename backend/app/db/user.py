from app.users.auth import get_hashed_password
from app.config import settings
from app.db.db_query import raw_query


def get_all_users() -> dict:
    return raw_query("SELECT id, first_name, last_name, birthday, gender, hobby, city FROM users;", False)


def get_user_by_id(id: int) -> dict:
    return raw_query(f"SELECT * FROM users WHERE id = {id};")


def find_user_by_login(login: str) -> dict:
    return raw_query(f"SELECT id FROM users WHERE login='{login}';")


# Sql select with no indexes
# def search_users(first_name: str, last_name: str) -> dict:
#     return db.query(f"SELECT id, first_name, last_name, birthday, gender, hobby, city FROM users "
#                     f"WHERE first_name LIKE '{first_name}%' AND last_name LIKE '{last_name}%';")


def search_users(first_name: str, last_name: str) -> dict:
    return raw_query(f"SELECT id, first_name, last_name, birthday, gender, hobby, city "
                     f"FROM users WHERE LOWER(first_name)::text LIKE '{first_name.lower()}%'"
                     f" AND LOWER(last_name)::text LIKE '{last_name.lower()}%';", False)


def auth_user(login: str) -> dict:
    result = raw_query(f"SELECT id, login, password FROM users WHERE login = '{login}';")
    return result if result else None


def create_user(first_name: str, last_name: str, login: str, password: str):
    raw_query(f"INSERT INTO users(first_name, last_name, login, password) "
             f"VALUES('{first_name}', "
             f"'{last_name}', "
             f"'{login}', "
             f"'{get_hashed_password(password)}');", True, settings.DB_PORT_WRITE)
    return find_user_by_login(login)


def get_user_friends(id: int):
    return raw_query(f"SELECT * FROM user_friends WHERE user_id = '{id}'", False)
