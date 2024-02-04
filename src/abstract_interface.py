from abc import ABC, abstractmethod

from src.ticket import Ticket


class AbstractInterface(ABC):
    @abstractmethod
    def print_closed_ticket(self, ticket: Ticket):
        pass

    @abstractmethod
    def print_form_close_ticket(self, ticket: Ticket):
        pass

    @abstractmethod
    def print_created_ticket(self, ticket: Ticket):
        pass

    @abstractmethod
    def print_form_create_ticket(self, ticket: Ticket):
        pass

    @abstractmethod
    def print_searched_ticket(self, ticket: Ticket):
        pass

    @abstractmethod
    def print_form_search_ticket(self, ticket: Ticket):
        pass

    @abstractmethod
    def print_updated_ticket(self, ticket: Ticket):
        pass

    @abstractmethod
    def print_form_update_ticket(self, ticket: Ticket):
        pass
