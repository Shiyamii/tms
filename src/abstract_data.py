from abc import ABC, abstractmethod
from typing import Optional
from src.ticket import Ticket


class AbstractData(ABC):
    """
    AbstractData is an abstract base class that defines the interface for data operations.
    """

    @abstractmethod
    def search_tickets(self, keyword) -> list[Ticket]:
        """
        Search for tickets using a keyword.

        :param keyword: The keyword to search for.
        :return: A list of Ticket objects that match the keyword.
        """
        pass

    @abstractmethod
    def get_ticket(self, ticket_id) -> Optional[Ticket]:
        """
        Get a ticket by its ID.

        :param ticket_id: The ID of the ticket.
        :return: The Ticket object with the given ID, or None if no such ticket exists.
        """
        pass

    @abstractmethod
    def id_exists(self, ticket_id) -> bool:
        """
        Check if a ticket ID exists.

        :param ticket_id: The ID of the ticket.
        :return: True if the ticket ID exists, False otherwise.
        """
        pass

    @abstractmethod
    def create_ticket(self, ticket) -> bool:
        """
        Create a new ticket.

        :param ticket: The Ticket object to create.
        :return: True if the ticket was created successfully, False otherwise.
        """
        pass

    @abstractmethod
    def update_ticket(self, ticket) -> bool:
        """
        Update an existing ticket.

        :param ticket: The Ticket object to update.
        :return: True if the ticket was updated successfully, False otherwise.
        """
        pass

    @abstractmethod
    def close_ticket(self, ticket) -> bool:
        """
        Close a ticket.

        :param ticket: The Ticket object to close.
        :return: True if the ticket was closed successfully, False otherwise.
        """
        pass

    @abstractmethod
    def get_old_new_ticket(self) -> list[Ticket]:
        """
        Get a list of NEW stated tickets older than 3 days.

        :return: A list of Ticket objects that are NEW stated and older than 3 days.
        """
        pass

    @abstractmethod
    def get_old_assigned_ticket(self) -> list[Ticket]:
        """
         Get a list of ASSIGNED stated tickets older than 10 days.

        :return: A list of Ticket objects that are ASSIGNED stated and older than 10 days.
        """
        pass

    @abstractmethod
    def get_old_ticket_list(self) -> list[Ticket]:
        """
        Get a list of tickets older than 20 days.

        :return: A list of Ticket objects that are older than 20 days.
        """
        pass
