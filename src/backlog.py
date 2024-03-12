from abc import ABC
from typing import Optional

from src.constants import State

from src.ticket import Ticket
from src.abstract_data import AbstractData


class Backlog(AbstractData, ABC):
    """
    This class represents a backlog of tickets stocked in the RAM.
    It provides methods to manage tickets such as creating, updating, closing, and searching for tickets.
    """

    def __init__(self):
        """
        Initialize a new instance of the Backlog class.
        """
        self.tickets: list[Ticket] = []
        self.deleted_tickets: list[Ticket] = []

    def search_tickets(self, keyword):
        """
        Search for tickets that match the given keyword.

        :param keyword: The keyword to search for.
        :return: A list of tickets that match the keyword.
        """
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
        """
        Get a ticket by its ID.

        :param ticket_id: The ID of the ticket to get.
        :return: The ticket with the given ID, or None if no such ticket exists.
        """
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                return ticket
        return None

    def id_exists(self, ticket_id) -> bool:
        """
        Check if a ticket with the given ID exists.

        :param ticket_id: The ID of the ticket to check.
        :return: True if a ticket with the given ID exists, False otherwise.
        """
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                return True
        return False

    def create_ticket(self, ticket) -> bool:
        """
        Create a new ticket.

        :param ticket: The ticket to create.
        :return: True if the ticket was created successfully, False otherwise.
        """
        if self.id_exists(ticket.id):
            return False
        self.tickets.append(ticket)
        return True

    def update_ticket(self, ticket) -> bool:
        """
        Update a ticket.

        :param ticket: The ticket to update.
        :return: True if the ticket was updated successfully, False otherwise.
        """
        for i in range(len(self.tickets)):
            if self.tickets[i].id == ticket.id:
                self.tickets[i].state = ticket.state
                self.tickets[i].responsible = ticket.responsible
                return True
        return False

    def close_ticket(self, ticket) -> bool:
        """
        Close a ticket.

        :param ticket: The ticket to close.
        :return: True if the ticket was closed successfully, False otherwise.
        """
        for i in range(len(self.tickets)):
            if self.tickets[i].id == ticket.id:
                self.tickets[i].state = ticket.state
                self.deleted_tickets.append(self.tickets.pop(i))
                return True
        return False

    def get_old_new_ticket(self) -> list[Ticket]:
        """
        Get a list of new tickets that are at least 3 days old.

        :return: A list of new tickets that are at least 3 days old.
        """
        return [
            ticket
            for ticket in self.tickets
            if ticket.state == State.NEW and ticket.get_age().days >= 3
        ]

    def get_old_assigned_ticket(self) -> list[Ticket]:
        """
        Get a list of assigned tickets that are at least 10 days old.

        :return: A list of assigned tickets that are at least 10 days old.
        """
        return [
            ticket
            for ticket in self.tickets
            if ticket.state == State.ASSIGNED and ticket.get_age().days >= 10
        ]

    def get_old_ticket_list(self) -> list[Ticket]:
        """
        Get a list of all tickets that are at least 20 days old.

        :return: A list of all tickets that are at least 20 days old.
        """
        return [ticket for ticket in self.tickets if ticket.get_age().days >= 20]
