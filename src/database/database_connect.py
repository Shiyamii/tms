import psycopg2
import os


class DatabaseConnect:
    """
    A class used to represent a database connection.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the DatabaseConnect object.

        :param self: An instance of the DatabaseConnect class.
        """
        self.connection = None

    def connect(self):
        """
        Connects to the database using environment variables.

        :param self: An instance of the DatabaseConnect class.
        """
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
        """
        Closes the connection to the database.

        :param self: An instance of the DatabaseConnect class.
        """
        self.connection.close()
        self.connection = None

    def execute(self, query, data=None):
        """
        Executes a query on the database.

        :param self: An instance of the DatabaseConnect class.
        :param query: The SQL query to execute.
        :param data: The data to use in the query.
        """
        cursor = self.connection.cursor()
        cursor.execute(query, data)
        self.connection.commit()
        cursor.close()

    def fetch(self, query, data=None):
        """
        Fetches all rows from a query.

        :param self: An instance of the DatabaseConnect class.
        :param query: The SQL query to fetch from.
        :param data: The data to use in the query.
        :return: The result of the fetch operation.
        """
        cursor = self.connection.cursor()
        cursor.execute(query, data)
        result = cursor.fetchall()
        cursor.close()
        return result

    def fetchone(self, query, data=None):
        """
        Fetches one row from a query.

        :param self: An instance of the DatabaseConnect class.
        :param query: The SQL query to fetch from.
        :param data: The data to use in the query.
        :return: The result of the fetch operation.
        """
        cursor = self.connection.cursor()
        cursor.execute(query, data)
        result = cursor.fetchone()
        cursor.close()
        return result
