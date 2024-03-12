from src.abstract_data import AbstractData
from src.database.database_connect import DatabaseConnect
from src.ticket import Ticket
from src.constants import State, Responsible, Type

from typing import Optional


class DB(AbstractData):
    def __init__(self, database_connection: DatabaseConnect):
        self.database_connection = database_connection
        self.database_connection.connect()

    @staticmethod
    def data_to_ticket(data):
        return Ticket(
            data[0],
            data[1],
            data[2],
            Type(data[3]),
            State(data[4]),
            Responsible(data[5]),
            data[6],
        )

    def data_to_tickets(self, data):
        return [self.data_to_ticket(ticket) for ticket in data]

    def search_tickets(self, keyword):
        query = """
            SELECT t.id,t.name,t.description,t.ticket_type,t.state,t.responsible,t.date_created 
            FROM ticket t 
            WHERE t.state != %s 
            AND(t.id LIKE %s  
            OR t.name LIKE %s
            OR t.description LIKE %s
            OR t.ticket_type LIKE %s
            OR t.state LIKE %s
            OR t.responsible LIKE %s)
        """
        data = (
            State.CLOSED.value,
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%",
        )
        result = self.database_connection.fetch(query, data)
        result = self.data_to_tickets(result)
        return result

    def get_ticket(self, ticket_id) -> Optional[Ticket]:
        query = """
            SELECT t.id,t.name,t.description,t.ticket_type,t.state,t.responsible,t.date_created 
            FROM  ticket t 
            WHERE t.id = %s AND t.state != %s 
        """
        data = (ticket_id, State.CLOSED.value)
        result = self.database_connection.fetchone(query, data)
        if result:
            return self.data_to_ticket(result)
        return None

    def id_exists(self, ticket_id) -> bool:
        query = "SELECT * FROM ticket WHERE id = %s AND state != %s"
        data = (ticket_id, State.CLOSED.value)
        result = self.database_connection.fetchone(query, data)
        return result is not None

    def create_ticket(self, ticket):
        query = """
            INSERT INTO ticket (id, name, description, ticket_type, state, responsible)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        data = (
            ticket.id,
            ticket.name,
            ticket.details,
            ticket.type.value,
            ticket.state.value,
            ticket.responsible.value,
        )
        self.database_connection.execute(query, data)

    def update_ticket(self, ticket):
        if not self.id_exists(ticket.id):
            return False
        query = """
            UPDATE ticket 
            SET name = %s, description = %s, ticket_type = %s, state = %s, responsible = %s
            WHERE id = %s
        """
        data = (
            ticket.name,
            ticket.details,
            ticket.type.value,
            ticket.state.value,
            ticket.responsible.value,
            ticket.id,
        )
        self.database_connection.execute(query, data)
        return True

    def close_ticket(self, ticket) -> bool:
        if not self.id_exists(ticket.id):
            return False
        query = """
            UPDATE ticket 
            SET state = %s
            WHERE id = %s
        """
        data = (State.CLOSED.value, ticket.id)
        self.database_connection.execute(query, data)

        return True

    def get_old_new_ticket(self) -> list[Ticket]:
        query = """
            SELECT t.id,t.name,t.description,t.ticket_type,t.state,t.responsible,t.date_created 
            FROM ticket t 
            WHERE t.state = %s AND t.date_created < NOW() - '3 days'::interval
        """
        data = (State.NEW.value,)
        result = self.database_connection.fetch(query, data)
        result = self.data_to_tickets(result)
        return result

    def get_old_assigned_ticket(self) -> list[Ticket]:
        query = """
            SELECT t.id,t.name,t.description,t.ticket_type,t.state,t.responsible,t.date_created 
            FROM ticket t 
            WHERE t.state = %s  AND t.date_created < NOW() - '10 days'::interval
        """
        data = (State.ASSIGNED.value,)
        result = self.database_connection.fetch(query, data)
        result = self.data_to_tickets(result)
        return result

    def get_old_ticket_list(self) -> list[Ticket]:
        query = """
            SELECT t.id,t.name,t.description,t.ticket_type,t.state,t.responsible,t.date_created 
            FROM ticket t 
            WHERE t.date_created < NOW() - '20 days'::interval
        """
        result = self.database_connection.fetch(query)
        result = self.data_to_tickets(result)
        return result
