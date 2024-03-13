import re

from src.abstract_interface import AbstractInterface
from src.abstract_data import AbstractData
from src.ticket import Ticket
from src.constants import State, Responsible, Type


class TMS:
    """
    This class represents the ticket management system.
    It provides methods to create, update, close, and search tickets.
    """

    def __init__(
        self, abstract_interface: AbstractInterface, abstract_data: AbstractData
    ):
        """
        Initialize a new instance of the TMS class.

        :param abstract_interface: The interface to use for user interaction.
        :param abstract_data: The data source to use for ticket management.
        """
        self.interface = abstract_interface
        self.data = abstract_data

    def close_ticket(self, case_id):
        """
        Close a ticket by its ID.

        :param case_id: The ID of the ticket to close.
        :return: True if the ticket was closed successfully, False otherwise.
        """
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

    def create_ticket(self, id, name, description, ticket_type):
        """
        Create a new ticket with the given details.

        :param id: The ID of the ticket.
        :param name: The name of the customer.
        :param description: The description of the ticket.
        :param ticket_type: The type of the ticket.
        :return: True if the ticket was created successfully, False otherwise.
        """
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

    def print_one_ticket(self, case_id):
        """
        Print the details of a ticket with the given ID.

        :param case_id: The ID of the ticket to print.
        :return: True if the ticket was found and printed, False otherwise.
        """
        ticket = self.data.get_ticket(case_id)
        if ticket is None:
            self.interface.print_ticket_invalid_id(case_id)
            return False
        self.interface.print_searched_ticket(ticket)
        return True

    def search_tickets(self, keyword):
        """
        Search for tickets using a keyword.

        :param keyword: The keyword to search for.
        :return: True if any tickets were found, False otherwise.
        """
        found = False
        self.interface.print_searched_keyword(keyword)
        tickets = self.data.search_tickets(keyword)
        if len(tickets) > 0:
            found = True
            self.interface.print_search(keyword, tickets)
        else:
            self.interface.print_keyword_not_found(keyword)
        return found

    def update_ticket(self, case_id, new_state, new_assign):
        """
        Update the state and responsible for a ticket.

        :param case_id: The ID of the ticket to update.
        :param new_state: The new state of the ticket.
        :param new_assign: The new assignee of the ticket.
        :return: True if the ticket was updated successfully, False otherwise.
        """
        new_state_enum = State.get_enum(new_state)
        if new_state_enum is None or (
            new_state_enum != State.ANALYSIS
            and new_state_enum != State.SOLVED
            and new_state_enum != State.IN_DELIVERY
            and new_state_enum != State.ASSIGNED
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

    def get_tar_3(self):
        """
        Get the old tickets for the TAR-3 report.

        :return: A dictionary containing the old tickets.
        """
        tickets_new_tar_3 = self.data.get_old_new_ticket()
        tickets_assigned_tar_3 = self.data.get_old_assigned_ticket()
        tickets_tar_3 = self.data.get_old_ticket_list()

        return {
            "new": {"tickets": tickets_new_tar_3, "count": len(tickets_new_tar_3)},
            "assigned": {
                "tickets": tickets_assigned_tar_3,
                "count": len(tickets_assigned_tar_3),
            },
            "all": {"tickets": tickets_tar_3, "count": len(tickets_tar_3)},
        }

    def main(self):
        """
        Run the main loop of the ticket management system.
        """

        while 1:
            val = self.interface.print_main_form()
            if val == "1":  # Create a ticket
                id, name, description, ticket_type = (
                    self.interface.print_form_create_ticket()
                )
                if id is not None:
                    self.create_ticket(id, name, description, ticket_type)
            elif val == "2":  # Assign a ticket
                id, state, assign_name = self.interface.print_form_update_ticket()
                if id is not None:
                    self.update_ticket(id, state, assign_name)
            elif val == "3":  # Close a ticket
                id = self.interface.print_form_close_ticket()
                if id is not None:
                    self.close_ticket(id)
            elif val == "4":  # Search issues
                keyword = self.interface.print_form_search_ticket()
                if keyword is not None:
                    self.search_tickets(keyword)
            elif val == "5":  # Display issue
                id = self.interface.print_one_form_ticket()
                if id is not None:
                    self.print_one_ticket(id)
            elif val == "6":  # Sortie
                tickets = self.get_tar_3()
                self.interface.print_tar_3_tickets(tickets)
            elif val == "7":  # Sortie
                break
            else:
                self.interface.print_invalid_selection()
