from app.db.sql import Database as data_base
from app.users.auth import get_hashed_password
from app.config import settings


def db_query(query: str, one_string_result=True, port=settings.DB_PORT_READ) -> dict:
    """
    :param query: Сырой SQL запрос
    :param one_string_result: Должна ли возвращаться одна строка или несколько
    :param port: По умолчанию 5000 порт для записи в базу 5001 для чтения
    :return:
    """
    db = data_base(settings.DB_NAME,
                   settings.DB_USER,
                   settings.DB_PASSWORD,
                   settings.DB_HOST,
                   port)
    if port == settings.DB_PORT_WRITE:
        db.insert(query)
    else:
        return db.query_one(query) if one_string_result else db.query(query)
    db.close()


def get_all_users() -> dict:
    return db_query("SELECT first_name, last_name, birthday, gender, hobby, city FROM users;", False)


def get_user_by_id(id: int) -> dict:
    return db_query(f"SELECT * FROM users WHERE id = {id};")


def find_user_by_login(login: str) -> dict:
    return db_query(f"SELECT id FROM users WHERE login='{login}';")



# Sql select with no indexes
# def search_users(first_name: str, last_name: str) -> dict:
#     return db.query(f"SELECT id, first_name, last_name, birthday, gender, hobby, city FROM users "
#                     f"WHERE first_name LIKE '{first_name}%' AND last_name LIKE '{last_name}%';")


def search_users(first_name: str, last_name: str) -> dict:
    return db_query(f"SELECT id, first_name, last_name, birthday, gender, hobby, city F"
                    f"ROM users WHERE LOWER(first_name)::text LIKE '{first_name.lower()}%'"
                    f" AND LOWER(last_name)::text LIKE '{last_name.lower()}%';", False)


def auth_user(login: str) -> dict:
    result = db_query(f"SELECT id, login, password FROM users WHERE login = '{login}';")
    return result if result else None


def create_user(first_name: str, last_name: str, login: str, password: str):
    db_query(f"INSERT INTO users(first_name, last_name, login, password) "
             f"VALUES('{first_name}', "
             f"'{last_name}', "
             f"'{login}', "
             f"'{get_hashed_password(password)}');", True, settings.DB_PORT_WRITE)
    return find_user_by_login(login)


def get_user_posts(id: int):
    return db_query(f"SELECT * FROM user_posts WHERE user_id = '{id}'", False)


def delete_user_post(id_user: int, id_post: int):
    return db_query(f"DELETE FROM user_posts WHERE user_id = '{id_user}' AND id = '{id_post}'",
                    True, settings.DB_PORT_WRITE)


def get_user_friends(id: int):
    return db_query(f"SELECT * FROM user_friends WHERE user_id = '{id}'", False)
