import psycopg2
from app.config import settings


# TODO Сделать обработку исключений на случай ошибки подключения к базе
class Database:
    def __init__(self, name, user, password, host, port):
        try:
            self.connect = psycopg2.connect(dbname=name,
                                            user=user,
                                            password=password,
                                            host=host,
                                            port=port)
            self.cursor = self.connect.cursor()
            print(f"Connected to PostgreSQL on {host}")
        except psycopg2.Error as e:
            print("Error connection to database", e)

    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self, insert_query):
        self.cursor.execute(insert_query)
        self.connect.commit()

    def close(self):
        self.cursor.close()
        self.connect.close()


db = Database(settings.DB_NAME,
              settings.DB_USER,
              settings.DB_PASSWORD,
              settings.DB_HOST,
              settings.DB_PORT)
