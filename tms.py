import re
import datetime
from enum import Enum


class State(Enum):
    NEW = "new"
    ANALYSIS = "analysis"
    SOLVED = "solved"
    IN_DELIVERY = "in_delivery"
    CLOSED = "closed"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class Responsible(Enum):
    L1 = "L1"
    L2 = "L2"
    L3 = "L3"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    # Get the ticket id from the user and close ticket status


def close_ticket(case_id, case_list, closed_list):
    print("Close ticket {}".format(case_id))
    for case in case_list:
        if case["id"] == case_id:
            if case["responsible"] != Responsible.L1.value:
                print("Only L1 can close the ticket")
                return False
            case["state"] = State.CLOSED.value
            case_list.remove(case)
            closed_list.append(case)
            return True
    print("Invalid id : ticket not found")
    return False


# Ticket creation with id,customer name and description
def create_ticket(id, name, description, type, case_list):
    if not re.match("^Case-\d\d\d$", id):
        raise Exception("ID is not in format Case-XXX where X represents a digit.")
    if len(id) == 0 or len(name) == 0 or len(description) == 0:
        raise Exception("One or more fields are empty, please fill all the details.")
    if not re.match("^\w+$", name):
        raise Exception("Name is not alphanumeric.")
    if type != "PR" and type != "IR":
        raise Exception("Type is not PR or IR.")
    for ticket in case_list:
        if ticket["id"] == id:
            raise Exception("ID already exists.")
    print("Create ticket {}".format(id))
    ticket = {}
    ticket["id"] = id
    ticket["name"] = name
    ticket["type"] = type
    ticket["details"] = description
    ticket["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ticket["state"] = State.NEW.value
    ticket["responsible"] = Responsible.L1.value
    case_list.append(ticket)


# get a issue and print the details of it
def print_one_ticket(case_id, case_list):
    print("Display one ticket information {}".format(case_id))
    for ticket in case_list:
        if ticket["id"] == case_id:
            print("Ticket ", "id : ", ticket["id"])
            print("Ticket ", "name : ", ticket["name"])
            print("Ticket ", "details : ", ticket["details"])
            print("Ticket ", "date : ", ticket["date"])
            print("Ticket ", "state : ", ticket["state"])
            print("Ticket ", "responsible : ", ticket["responsible"])
            return True
    print("Invalid id : ticket not found")
    return False


# Get a keyword from user and search issues that contain that substring
def search_tickets(keyword, case_list):
    found = False
    print("Search keyword {}".format(keyword))
    for ticket in case_list:
        if (
            keyword in ticket["id"]
            or keyword in ticket["name"]
            or keyword in ticket["details"]
            or keyword in ticket["type"]
            or keyword in ticket["state"]
            or keyword in ticket["responsible"]
        ):
            print_one_ticket(ticket["id"], case_list)
            print("")
            found = True
    if not found:
        print("Keyword {} not found".format(keyword))
    return found


# Update an issue in backlog
def update_ticket(case_id, new_state, new_assign, ticketlist):
    if new_state != "" and (
        new_state != State.ANALYSIS.value
        and new_state != State.SOLVED.value
        and new_state != State.IN_DELIVERY.value
    ):
        print("Invalid state {}".format(new_state))
        return False
    if new_assign != "" and Responsible.has_value(new_assign) is False:
        print("Invalid assign {}".format(new_assign))
        return False
    print("Assign ticket {} to {}".format(case_id, new_assign))
    for ticket in ticketlist:
        if ticket["id"] == case_id:
            if new_state != "":
                ticket["state"] = new_state
            if new_assign != "":
                ticket["responsible"] = new_assign
            return True
    print("Invalid id {} : ticket does not exists".format(case_id))
    return False


if __name__ == "__main__":
    # An infinite loop for menu that constantly asks user for their selection
    # Does operations selected by the input
    backlog = []
    closed_backlog = []

    while 1:
        print("\n1. Create a ticket")
        print("2. Update a ticket")
        print("3. Close a ticket")
        print("4. Search keyword")
        print("5. Display issue from backlog")
        print("6. Sortie")

        val = input("\nEnter your selection: ")
        if val == "1":  # Create a ticket
            id = input("Id: ")
            name = input("Customer name: ")
            description = input("Case description: ")
            type = input("Case type: ")
            # Detect problems in createIssue function and display error message to user
            try:
                create_ticket(id, name, description, type, backlog)
            except Exception as exception:
                print("Error while creating a new issue:" + str(exception))
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
