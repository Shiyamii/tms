from database.database_connect import DatabaseConnect

create_table_ticket = """
    CREATE TABLE IF NOT EXISTS ticket (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    ticket_type TEXT NOT NULL,
    state TEXT NOT NULL,
    responsible TEXT NOT NULL,
    date_created TIMESTAMP NOT NULL DEFAULT NOW()
);
"""


if __name__ == "__main__":
    database_connection = DatabaseConnect()
    database_connection.connect()
    database_connection.execute(create_table_ticket)
    print("Tables created successfully")
    database_connection.disconnect()
