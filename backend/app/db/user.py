from app.db.sql import Database as data_base
from app.users.auth import get_hashed_password
from app.config import settings


def db_query_read(query: str) -> dict:
    db = data_base(settings.DB_NAME,
                  settings.DB_USER,
                  settings.DB_PASSWORD,
                  settings.DB_HOST,
                  settings.DB_PORT)
    result = db.query_one(query)
    print("data")
    db.close()
    return result


def get_all_users() -> dict:
    return db_query_read("SELECT first_name, last_name, birthday, gender, hobby, city FROM users;")


def get_user_by_id(id: int) -> dict:
    return db_query_read(f"SELECT * FROM users WHERE id = {id};")


def find_user_by_login(login: str) -> dict:
    result = db_query_read(f"SELECT id FROM users WHERE login='{login}';")
    return result[0] if result else None

# Sql select with no indexes
# def search_users(first_name: str, last_name: str) -> dict:
#     return db.query(f"SELECT id, first_name, last_name, birthday, gender, hobby, city FROM users "
#                     f"WHERE first_name LIKE '{first_name}%' AND last_name LIKE '{last_name}%';")


def search_users(first_name: str, last_name: str) -> dict:
    return db_query_read(f"SELECT id, first_name, last_name, birthday, gender, hobby, city F"
                    f"ROM users WHERE LOWER(first_name)::text LIKE '{first_name.lower()}%'"
                    f" AND LOWER(last_name)::text LIKE '{last_name.lower()}%';")


def auth_user(login: str) -> dict:
    result = db_query_read(f"SELECT id, login, password FROM users WHERE login = '{login}';")
    return result[0] if result else None


def create_user(first_name: str, last_name: str, login: str, password: str):
    db.insert(f"INSERT INTO users(first_name, last_name, login, password) "
              f"VALUES('{first_name}', "
              f"'{last_name}', "
              f"'{login}', "
              f"'{get_hashed_password(password)}');")
    return find_user_by_login(login)