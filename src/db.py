from src.abstract_data import AbstractData
from database.database_connect import DatabaseConnect
from src.ticket import Ticket
from src.constants import State, Responsible, Type

from typing import Optional


class DB(AbstractData):
    def __init__(self):
        self.database_connection = DatabaseConnect()
        self.database_connection.connect()
        print(self.get_ticket("Case-011"))
        print(self.get_ticket("1"))

    @staticmethod
    def data_to_ticket(data):
        print(data)
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
        print(data)
        return [self.data_to_ticket(ticket) for ticket in data]

    def search_tickets(self, keyword):
        query = """
            SELECT t.id,t.name,t.description,t.ticket_type,t.state,t.responsible,b.date_created 
            FROM backlog b, ticket t 
            WHERE b.ticket_id = t.id 
            AND (t.id LIKE %s 
            OR t.name LIKE %s 
            OR t.description LIKE %s
            OR t.ticket_type LIKE %s
            OR t.state LIKE %s
            OR t.responsible LIKE %s)
        """
        data = (
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
            SELECT t.id,t.name,t.description,t.ticket_type,t.state,t.responsible,b.date_created 
            FROM backlog b, ticket t 
            WHERE b.ticket_id = t.id 
            AND t.id = %s
        """
        data = (ticket_id,)
        result = self.database_connection.fetchone(query, data)
        if result:
            return self.data_to_ticket(result)
        return None

    def id_exists(self, ticket_id) -> bool:
        pass

    def create_ticket(self, ticket):
        query = """
            INSERT INTO ticket (id, name, description, ticket_type, state, responsible)
            VALUES (%s, %s, %s, %s, %s, %s)
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
        pass

    def close_ticket(self, ticket) -> bool:
        pass
