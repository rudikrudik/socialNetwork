import psycopg, time


class Database:
    def __init__(self, name, user, password, host, port):
        self.db_name = name
        self.db_user = user
        self.db_password = password
        self.db_host = host
        self.db_port = port
        self.connect = psycopg.connect(dbname=self.db_name,
                                       user=self.db_user,
                                       password=self.db_password,
                                       host=self.db_host,
                                       port=self.db_port)
        self.cursor = self.connect.cursor()

    def close(self):
        self.cursor.close()
        self.connect.close()

    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def query_one(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def insert(self, insert_query):
        self.cursor.execute(insert_query)
        self.connect.commit()
