from abc import ABC, abstractmethod

from src.ticket import Ticket


class AbstractInterface(ABC):
    """
    Abstract base class that defines the interface for ticket operations.
    """

    @abstractmethod
    def print_close_ticket(self, case_id):
        """
        Print the details of a closed ticket.

        :param case_id: The ID of the ticket.
        """
        pass

    @abstractmethod
    def print_form_close_ticket(self):
        """
        Print the form for closing a ticket.
        """
        pass

    @abstractmethod
    def print_l1_close_ticket(self):
        """
        Print the form for closing a ticket.
        """
        pass

    @abstractmethod
    def print_created_ticket(self, ticket: Ticket):
        """
        Print the details of a newly created ticket.

        :param ticket: The ticket object.
        """
        pass

    @abstractmethod
    def print_form_create_ticket(self):
        """
        Print the form for creating a new ticket.
        """
        pass

    @abstractmethod
    def print_searched_ticket(self, ticket: Ticket):
        """
        Print the details of a searched ticket.

        :param ticket: The ticket object.
        """
        pass

    @abstractmethod
    def print_ticket_invalid_id(self, case_id):
        """
        Print an error message for an invalid ticket ID.

        :param case_id: The ID of the ticket.
        """
        pass

    @abstractmethod
    def print_form_search_ticket(self):
        """
        Print the form for searching a ticket.
        """
        pass

    @abstractmethod
    def print_searched_keyword(self, keyword):
        """
        Print the keyword used for searching tickets.

        :param keyword: The keyword used for searching.
        """
        pass

    @abstractmethod
    def print_keyword_not_found(self, keyword):
        """
        Print an error message when the keyword is not found in any ticket.

        :param keyword: The keyword used for searching.
        """
        pass

    @abstractmethod
    def print_updated_ticket(self, case_id, new_assign, new_state):
        """
        Print the details of an updated ticket.

        :param case_id: The ID of the ticket.
        :param new_assign: The new assignee of the ticket.
        :param new_state: The new state of the ticket.
        """
        pass

    @abstractmethod
    def print_form_update_ticket(self):
        """
        Print the form for updating a ticket.
        """
        pass

    @abstractmethod
    def print_one_form_ticket(self):
        """
        Print the form for a single ticket.
        """
        pass

    @abstractmethod
    def print_main_form(self):
        """
        Print the main form of the application.
        """
        pass

    @abstractmethod
    def print_invalid_selection(self):
        """
        Print an error message for an invalid selection.
        """
        pass

    @abstractmethod
    def print_invalid_id(self):
        """
        Print an error message for an invalid ID.
        """
        pass

    @abstractmethod
    def print_invalid_name(self):
        """
        Print an error message for an invalid name.
        """
        pass

    @abstractmethod
    def print_invalid_details(self):
        """
        Print an error message for invalid details.
        """
        pass

    @abstractmethod
    def print_invalid_type(self):
        """
        Print an error message for an invalid ticket type.
        """
        pass

    @abstractmethod
    def print_invalid_state(self, new_state):
        """
        Print an error message for an invalid state.

        :param new_state: The new state of the ticket.
        """
        pass

    @abstractmethod
    def print_invalid_responsible(self, new_assign):
        """
        Print an error message for an invalid responsible person.

        :param new_assign: The new assignee of the ticket.
        """
        pass

    @abstractmethod
    def print_id_already_exists(self):
        """
        Print an error message when the ticket ID already exists.
        """
        pass

    @abstractmethod
    def print_tar_3_tickets(self, tickets):
        """
        Print the details of the old tickets respecting the TAR-3.

        :param tickets: The list of ticket objects.
        """
        pass

    @abstractmethod
    def print_search(self, keyword, tickets):
        """
        Print the results of a ticket search.

        :param keyword: The keyword used for searching.
        :param tickets: The list of ticket objects.
        """
        pass
