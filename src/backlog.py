from typing import Optional

from src.ticket import Ticket
from src.abstract_data import AbstractData


class Backlog(AbstractData):
    def __init__(self):
        self.tickets: list[Ticket] = []
        self.deleted_tickets: list[Ticket] = []

    def search_tickets(self, keyword):
        tickets = []
        for ticket in self.tickets:
            if (
                keyword in ticket.id
                or keyword in ticket.name
                or keyword in ticket.type.value
                or keyword in ticket.details
                or keyword in ticket.state.value
                or keyword in ticket.responsible.value
            ):
                tickets.append(ticket)
        return tickets

    def get_ticket(self, ticket_id) -> Optional[Ticket]:
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                return ticket
        return None

    def id_exists(self, ticket_id) -> bool:
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                return True
        return False

    def create_ticket(self, ticket) -> bool:
        if self.id_exists(ticket.id):
            return False
        self.tickets.append(ticket)
        return True

    def update_ticket(self, ticket) -> bool:
        for i in range(len(self.tickets)):
            if self.tickets[i].id == ticket.id:
                self.tickets[i].state = ticket.state
                self.tickets[i].responsible = ticket.responsible
                return True
        return False

    def close_ticket(self, ticket) -> bool:
        for i in range(len(self.tickets)):
            if self.tickets[i].id == ticket.id:
                self.tickets[i].state = ticket.state
                self.deleted_tickets.append(self.tickets.pop(i))
                return True
        return False
