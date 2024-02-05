import re

from src.interface import Interface
from src.ticket import Ticket
from src.constants import State, Responsible, Type

interface = Interface()


def close_ticket(case_id, case_list: list[Ticket], closed_list: list[Ticket]):
    interface.print_close_ticket(case_id)
    for case in case_list:
        if case.id == case_id:
            if case.responsible != Responsible.L1:
                interface.print_l1_close_ticket()
                return False
            case.state = State.CLOSED
            case_list.remove(case)
            closed_list.append(case)
            return True
    interface.print_ticket_invalid_id(case_id)
    return False


# Ticket creation with id,customer name and description
def create_ticket(id, name, description, type, case_list: list[Ticket]):
    if not re.match("^Case-\d\d\d$", id):
        interface.print_invalid_id()
        return False
    if len(description) == 0:
        interface.print_invalid_details()
        return False
    if not re.match("^\w+$", name):
        interface.print_invalid_name()
        return False
    type = Type.get_enum(type)
    if type is None:
        interface.print_invalid_type()
        return False
    for ticket in case_list:
        if ticket.id == id:
            interface.print_id_already_exists()
            return False
    ticket = Ticket(id, name, description, type, State.NEW, Responsible.L1)
    interface.print_created_ticket(ticket)
    case_list.append(ticket)
    return True


# get a issue and print the details of it
def print_one_ticket(case_id, case_list):
    for ticket in case_list:
        if ticket.id == case_id:
            interface.print_searched_ticket(ticket)
            return True
    interface.print_ticket_invalid_id(case_id)
    return False


# Get a keyword from user and search issues that contain that substring
def search_tickets(keyword, case_list):
    found = False
    interface.print_searched_keyword(keyword)
    for ticket in case_list:
        if (
            keyword in ticket.id
            or keyword in ticket.name
            or keyword in ticket.type.value
            or keyword in ticket.details
            or keyword in ticket.state.value
            or keyword in ticket.responsible.value
        ):
            interface.print_searched_ticket(ticket)
            found = True
    if not found:
        interface.print_keyword_not_found(keyword)
    return found


# Update an issue in backlog
def update_ticket(case_id, new_state, new_assign, ticketlist):
    new_state_enum = State.get_enum(new_state)
    if new_state_enum is None or (
        new_state_enum != State.ANALYSIS
        and new_state_enum != State.SOLVED
        and new_state_enum != State.IN_DELIVERY
    ):
        interface.print_invalid_state(new_state)
        return False
    new_assign_enum = Responsible.get_enum(new_assign)
    if new_state is None:
        interface.print_invalid_responsible(new_assign)
        return False
    interface.print_updated_ticket(case_id, new_assign, new_state)
    for ticket in ticketlist:
        if ticket.id == case_id:
            ticket.state = new_state_enum
            ticket.responsible = new_assign_enum
            return True
    interface.print_ticket_invalid_id(case_id)
    return False


def main():
    # An infinite loop for menu that constantly asks user for their selection
    # Does operations selected by the input
    backlog = []
    closed_backlog = []

    while 1:
        val = interface.print_main_form()
        if val == "1":  # Create a ticket
            id, name, description, type = interface.print_form_create_ticket()
            # Detect problems in createIssue function and display error message to user

            create_ticket(id, name, description, type, backlog)
        elif val == "2":  # Assign a ticket
            id, state, assign_name = interface.print_form_update_ticket()
            update_ticket(id, state, assign_name, backlog)
        elif val == "3":  # Close a ticket
            id = interface.print_form_close_ticket()
            close_ticket(id, backlog, closed_backlog)
        elif val == "4":  # Search issues
            keyword = interface.print_form_search_ticket()
            search_tickets(keyword, backlog)
        elif val == "5":  # Display issue
            id = interface.print_one_form_ticket()
            print_one_ticket(id, backlog)
        elif val == "6":  # Sortie
            break
        else:
            interface.print_invalid_selection()
