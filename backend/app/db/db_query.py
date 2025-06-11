from app.db.sql import Database as data_base
from app.config import settings


def raw_query(query: str, one_string_result=True, port=settings.DB_PORT_READ) -> dict:
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
