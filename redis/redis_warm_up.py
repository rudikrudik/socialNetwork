import psycopg
import redis
import json

config_dict = {}


def read_config() -> None:
    try:
        with open("config.env", "r", encoding="utf-8") as file:
            for line in file:
                key, value = line.split("=")
                config_dict[key] = value.strip("\n")
    except FileNotFoundError as error:
        print("Config file not found ", error)


def get_data_from_sql() -> list:
    try:
        with psycopg.connect(
            dbname=config_dict["DB_NAME"],
            user=config_dict["DB_USER"],
            password=config_dict["DB_PASSWORD"],
            host=config_dict["DB_HOST"],
            port=config_dict["DB_PORT_READ"]
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM user_posts ORDER BY post_date_create DESC LIMIT 1000")
                return cur.fetchall()
    except psycopg.errors as error:
        print("Error connect to PostgreSQL ", error)


def redis_db_set_warm_up_data() -> None:
    posts = get_data_from_sql()

    try:
        with redis.Redis(host=config_dict["REDIS_CACHE_HOST"],
                         port=config_dict["REDIS_CACHE_PORT"],
                         db=config_dict["REDIS_DB"],
                         password=config_dict["REDIS_PASSWORD"]
                         ) as redis_connect:
            with redis_connect as r_connect:
                for post in posts:
                    sql_str = json.dumps(post, indent=4, sort_keys=True, default=str, ensure_ascii=False)
                    r_connect.hset(str(post[0]), str(post[0]), sql_str)
    except redis.exceptions as error:
        print("Error connect to Redis service ", error)


read_config()
redis_db_set_warm_up_data()
