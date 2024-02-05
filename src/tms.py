import re

from src.interface import Interface
from src.ticket import Ticket
from src.constants import State, Responsible, Type

interface = Interface()


def close_ticket(case_id, case_list: list[Ticket], closed_list: list[Ticket]):
    print("Close ticket {}".format(case_id))
    for case in case_list:
        if case.id == case_id:
            if case.responsible != Responsible.L1:
                print("Only L1 can close the ticket")
                return False
            case.state = State.CLOSED
            case_list.remove(case)
            closed_list.append(case)
            return True
    print("Invalid id : ticket not found")
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
    interface.print_ticket_invalid_id()
    return False


# Get a keyword from user and search issues that contain that substring
def search_tickets(keyword, case_list):
    found = False
    print("Search keyword {}".format(keyword))
    for ticket in case_list:
        if (
            keyword in ticket.id
            or keyword in ticket.name
            or keyword in ticket.type.value
            or keyword in ticket.details
            or keyword in ticket.state.value
            or keyword in ticket.responsible.value
        ):
            print_one_ticket(ticket.id, case_list)
            print("")
            found = True
    if not found:
        print("Keyword {} not found".format(keyword))
    return found


# Update an issue in backlog
def update_ticket(case_id, new_state: State, new_assign: Responsible, ticketlist):
    if new_state != "" and (
        (not isinstance(new_state, State))
        or (
            new_state != State.ANALYSIS
            and new_state != State.SOLVED
            and new_state != State.IN_DELIVERY
        )
    ):
        print("Invalid state {}".format(new_state))
        return False
    if new_assign != "" and not isinstance(new_assign, Responsible):
        print("Invalid assign {}".format(new_assign))
        return False
    print("Assign ticket {} to {}".format(case_id, new_assign))
    for ticket in ticketlist:
        if ticket.id == case_id:
            if new_state != "":
                ticket.state = new_state
            if new_assign != "":
                ticket.responsible = new_assign
            return True
    print("Invalid id {} : ticket does not exists".format(case_id))
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
            id = input("Id: ")
            state = input("State: ")
            assign_name = input("Assigned to: ")
            update_ticket(id, state, assign_name, backlog)
        elif val == "3":  # Close a ticket
            id = input("Id: ")
            close_ticket(id, backlog, closed_backlog)
        elif val == "4":  # Search issues
            keyword = input("Keyword: ")
            search_tickets(keyword, backlog)
        elif val == "5":  # Display issue
            Id = input("Id: ")
            print_one_ticket(Id, backlog)
        elif val == "6":  # Sortie
            break
        else:
            print("Invalid selection")
