from src.abstract_interface import AbstractInterface
from src.ticket import Ticket


class Interface(AbstractInterface):
    def print_closed_ticket(self, ticket):
        print("Ticket closed: ", ticket)

    def print_form_close_ticket(self):
        id = input("Id: ")
        return id

    def print_created_ticket(self, ticket):
        print("Ticket created: ", ticket.id)

    def print_form_create_ticket(self):
        id = input("Id: ")
        name = input("Customer name: ")
        description = input("Case description: ")
        type = input("Case type: ")
        return id, name, description, type

    def print_searched_ticket(self, ticket):
        self.print_one_ticket(ticket)

    def print_form_search_ticket(self):
        keyword = input("Keyword: ")
        return keyword

    def print_ticket_invalid_id(self):
        print("Invalid id : ticket not found")

    def print_updated_ticket(self, ticket):
        print("Ticket updated: ", ticket)

    def print_form_update_ticket(self):
        id = input("Id: ")
        state = input("State: ")
        assign_name = input("Assigned to: ")
        return id, state, assign_name

    def print_main_form(self):
        print("\n1. Create a ticket")
        print("2. Update a ticket")
        print("3. Close a ticket")
        print("4. Search keyword")
        print("5. Display issue from backlog")
        print("6. Sortie")

        val = input("\nEnter your selection: ")
        return val

    def print_one_ticket(self, ticket: Ticket):
        print("Ticket ", "id : ", ticket.id)
        print("Ticket ", "name : ", ticket.name)
        print("Ticket ", "details : ", ticket.details)
        print("Ticket ", "date : ", ticket.date)
        print("Ticket ", "state : ", ticket.state)
        print("Ticket ", "responsible : ", ticket.responsible)

    def print_invalid_id(self):
        print("ID is not in format Case-XXX where X represents a digit.")

    def print_invalid_name(self):
        print("Name is empty or is not alphanumeric")

    def print_invalid_details(self):
        print("Description are empty, please fill all the details.")

    def print_invalid_type(self):
        print("Type is not PR or IR.")

    def print_invalid_state(self):
        print("State is not NEW, ANALYSIS, SOLVED, IN_DELIVERY or CLOSED.")

    def print_invalid_responsible(self):
        print("Responsible is not L1, L2 or L3.")

    def print_id_already_exists(self):
        print("ID already exists")