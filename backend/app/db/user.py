from app.db.sql import db
from app.users.auth import get_hashed_password


def get_all_users() -> dict:
    return db.query("SELECT first_name, last_name, birthday, gender, hobby, city FROM users;")


def get_user_by_id(id: int) -> dict:
    result = db.query(f"SELECT * FROM users WHERE id = {id};")
    return result[0] if result else None


def find_user_by_login(login: str) -> dict:
    result = db.query(f"SELECT id FROM users WHERE login='{login}';")
    return result[0] if result else None


def auth_user(login: str) -> dict:
    result = db.query(f"SELECT id, login, password FROM users WHERE login = '{login}';")
    return result[0] if result else None


def create_user(first_name: str, last_name: str, login: str, password: str):
    db.insert(f"INSERT INTO users(first_name, last_name, login, password) "
              f"VALUES('{first_name}', "
              f"'{last_name}', "
              f"'{login}', "
              f"'{get_hashed_password(password)}');")
    return find_user_by_login(login)