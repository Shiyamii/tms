from abc import ABC, abstractmethod

from src.ticket import Ticket


class AbstractInterface(ABC):
    @abstractmethod
    def print_close_ticket(self, case_id):
        pass

    @abstractmethod
    def print_form_close_ticket(self):
        pass

    @abstractmethod
    def print_l1_close_ticket(self):
        pass

    @abstractmethod
    def print_created_ticket(self, ticket: Ticket):
        pass

    @abstractmethod
    def print_form_create_ticket(self):
        pass

    @abstractmethod
    def print_searched_ticket(self, ticket: Ticket):
        pass

    @abstractmethod
    def print_ticket_invalid_id(self, case_id):
        pass

    @abstractmethod
    def print_form_search_ticket(self):
        pass

    @abstractmethod
    def print_searched_keyword(self, keyword):
        pass

    @abstractmethod
    def print_keyword_not_found(self, keyword):
        pass

    @abstractmethod
    def print_updated_ticket(self, case_id, new_assign, new_state):
        pass

    @abstractmethod
    def print_form_update_ticket(self):
        pass

    @abstractmethod
    def print_one_form_ticket(self):
        pass

    @abstractmethod
    def print_main_form(self):
        pass

    @abstractmethod
    def print_invalid_selection(self):
        pass

    @abstractmethod
    def print_invalid_id(self):
        pass

    @abstractmethod
    def print_invalid_name(self):
        pass

    @abstractmethod
    def print_invalid_details(self):
        pass

    @abstractmethod
    def print_invalid_type(self):
        pass

    @abstractmethod
    def print_invalid_state(self, new_state):
        pass

    @abstractmethod
    def print_invalid_responsible(self, new_assign):
        pass

    @abstractmethod
    def print_id_already_exists(self):
        pass
