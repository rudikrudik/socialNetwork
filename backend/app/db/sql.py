import psycopg, time
from app.config import settings


class Database:
    def __init__(self, name, user, password, host, port):
        for i in range(1, 6):
            try:
                self.connect = psycopg.connect(dbname=name,
                                                user=user,
                                                password=password,
                                                host=host,
                                                port=port)
                self.cursor = self.connect.cursor()
                check_error = None
            except psycopg.Error as error:
                print(f"Retry to connect to database. Attempt: {i}")
                check_error = error
            if i == 5:
                raise check_error
            if check_error:
                time.sleep(5)
            else:
                print(f"Success connect to database. Attempt: {i}")
                break

    def close(self):
        self.cursor.close()
        self.connect.close()

    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def query_one(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except psycopg.OperationalError as error:
            self.close()
            raise RuntimeError('Failed to open database') from error

    def insert(self, insert_query):
        self.cursor.execute(insert_query)
        self.connect.commit()

db = Database(settings.DB_NAME,
              settings.DB_USER,
              settings.DB_PASSWORD,
              settings.DB_HOST,
              settings.DB_PORT)
