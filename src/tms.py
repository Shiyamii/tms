import re

from src.abstract_interface import AbstractInterface
from src.abstract_data import AbstractData
from src.ticket import Ticket
from src.constants import State, Responsible, Type


class TMS:
    def __init__(
        self, abstract_interface: AbstractInterface, abstract_data: AbstractData
    ):
        self.interface = abstract_interface
        self.data = abstract_data

    def close_ticket(self, case_id):
        self.interface.print_close_ticket(case_id)
        ticket = self.data.get_ticket(case_id)
        if ticket is None:
            self.interface.print_ticket_invalid_id(case_id)
            return False
        if ticket.responsible != Responsible.L1:
            self.interface.print_l1_close_ticket()
            return False
        ticket.state = State.CLOSED
        self.data.close_ticket(ticket)
        return True

    # Ticket creation with id,customer name and description
    def create_ticket(self, id, name, description, ticket_type):
        if not re.match("^Case-\d\d\d$", id):
            self.interface.print_invalid_id()
            return False
        if len(description) == 0:
            self.interface.print_invalid_details()
            return False
        if not re.match("^\w+$", name):
            self.interface.print_invalid_name()
            return False
        ticket_type_enum = Type.get_enum(ticket_type)
        if ticket_type_enum is None:
            self.interface.print_invalid_type()
            return False
        if self.data.id_exists(id):
            self.interface.print_id_already_exists()
            return False
        ticket = Ticket(
            id, name, description, ticket_type_enum, State.NEW, Responsible.L1
        )
        self.interface.print_created_ticket(ticket)
        self.data.create_ticket(ticket)
        return True

    # get an issue and print the details of it
    def print_one_ticket(self, case_id):
        ticket = self.data.get_ticket(case_id)
        if ticket is None:
            self.interface.print_ticket_invalid_id(case_id)
            return False
        self.interface.print_searched_ticket(ticket)
        return True

    # Get a keyword from user and search issues that contain that substring
    def search_tickets(self, keyword):
        found = False
        self.interface.print_searched_keyword(keyword)
        tickets = self.data.search_tickets(keyword)
        for ticket in tickets:
            self.interface.print_searched_ticket(ticket)
            found = True

        if not found:
            self.interface.print_keyword_not_found(keyword)
        return found

    # Update an issue in backlog
    def update_ticket(self, case_id, new_state, new_assign):
        new_state_enum = State.get_enum(new_state)
        if new_state_enum is None or (
            new_state_enum != State.ANALYSIS
            and new_state_enum != State.SOLVED
            and new_state_enum != State.IN_DELIVERY
        ):
            self.interface.print_invalid_state(new_state)
            return False
        new_assign_enum = Responsible.get_enum(new_assign)
        if new_assign_enum is None:
            self.interface.print_invalid_responsible(new_assign)
            return False
        self.interface.print_updated_ticket(case_id, new_assign, new_state)
        ticket = self.data.get_ticket(case_id)
        if ticket is None:
            self.interface.print_ticket_invalid_id(case_id)
            return False
        ticket.state = new_state_enum
        ticket.responsible = new_assign_enum
        self.data.update_ticket(ticket)
        return True

    def main(self):
        # An infinite loop for menu that constantly asks user for their selection
        # Does operations selected by the input

        while 1:
            val = self.interface.print_main_form()
            if val == "1":  # Create a ticket
                id, name, description, ticket_type = (
                    self.interface.print_form_create_ticket()
                )
                self.create_ticket(id, name, description, ticket_type)
            elif val == "2":  # Assign a ticket
                id, state, assign_name = self.interface.print_form_update_ticket()
                if id is not None:
                    self.update_ticket(id, state, assign_name)
            elif val == "3":  # Close a ticket
                id = self.interface.print_form_close_ticket()
                self.close_ticket(id)
            elif val == "4":  # Search issues
                keyword = self.interface.print_form_search_ticket()
                self.search_tickets(keyword)
            elif val == "5":  # Display issue
                id = self.interface.print_one_form_ticket()
                if id is not None:
                    self.print_one_ticket(id)
            elif val == "6":  # Sortie
                break
            else:
                self.interface.print_invalid_selection()
