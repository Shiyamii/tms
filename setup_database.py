from database.database_connect import DatabaseConnect

create_table_ticket = """
    CREATE TABLE IF NOT EXISTS ticket (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    ticket_type TEXT NOT NULL,
    state TEXT NOT NULL,
    responsible TEXT NOT NULL
);
"""

create_table_backlog = """
    CREATE TABLE IF NOT EXISTS backlog (
    id SERIAL PRIMARY KEY,
    date_created TIMESTAMP NOT NULL,
    ticket_id TEXT NOT NULL,
    FOREIGN KEY (ticket_id) REFERENCES ticket(id)
);
"""

create_table_deleted_backlog = """
    CREATE TABLE IF NOT EXISTS deleted_backlog (
    id SERIAL PRIMARY KEY,
    date_created TIMESTAMP NOT NULL,
    ticket_id TEXT NOT NULL,
    FOREIGN KEY (ticket_id) REFERENCES ticket(id)
);
"""


if __name__ == "__main__":
    database_connection = DatabaseConnect()
    database_connection.connect()
    database_connection.execute(create_table_ticket)
    database_connection.execute(create_table_backlog)
    database_connection.execute(create_table_deleted_backlog)
    print("Tables created successfully")
    database_connection.disconnect()
