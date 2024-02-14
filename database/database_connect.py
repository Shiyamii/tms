import psycopg2
import os


class DatabaseConnect:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=os.getenv("DATABASE_NAME"),
                user=os.getenv("DATABASE_USER"),
                password=os.getenv("DATABASE_PASSWORD"),
                host=os.getenv("DATABASE_HOST"),
                port=os.getenv("DATABASE_PORT"),
            )
            self.connection.autocommit = True
        except Exception as e:
            print(f"Error: {e}")

    def disconnect(self):
        self.connection.close()
        self.connection = None

    def execute(self, query, data=None):
        cursor = self.connection.cursor()
        cursor.execute(query, data)
        self.connection.commit()
        cursor.close()

    def fetch(self, query, data=None):
        cursor = self.connection.cursor()
        cursor.execute(query, data)
        result = cursor.fetchall()
        cursor.close()
        return result

    def fetchone(self, query, data=None):
        cursor = self.connection.cursor()
        cursor.execute(query, data)
        result = cursor.fetchone()
        cursor.close()
        return result
