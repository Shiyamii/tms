from src.abstract_interface import AbstractInterface
from src.ticket import Ticket


class Interface(AbstractInterface):
    """
    This class provides an console interface for interacting with the ticket system.
    """

    def print_close_ticket(self, case_id):
        """
        Print a message indicating that a ticket has been closed.

        :param case_id: The ID of the closed ticket.
        """
        print("Close ticket {}".format(case_id))

    def print_form_close_ticket(self):
        """
        Prompt the user to enter the ID of the ticket to close.

        :return: The ID of the ticket to close.
        """
        id = input("Id: ")
        return id

    def print_l1_close_ticket(self):
        """
        Print a message indicating that only L1 can close the ticket.
        """
        print("Only L1 can close the ticket")

    def print_created_ticket(self, ticket):
        """
        Print a message indicating that a ticket has been created.

        :param ticket: The created ticket.
        """
        print("Ticket created: ", ticket.id)

    def print_form_create_ticket(self):
        """
        Prompt the user to enter the details of the ticket to create.

        :return: The details of the ticket to create.
        """
        id = input("Id: ")
        name = input("Customer name: ")
        description = input("Case description: ")
        ticket_type = input("Case type: ")
        return id, name, description, ticket_type

    def print_searched_ticket(self, ticket):
        """
        Print the details of a ticket.

        :param ticket: The ticket to print.
        """
        self.print_one_ticket(ticket)

    def print_form_search_ticket(self):
        """
        Prompt the user to enter a keyword to search for.

        :return: The keyword to search for.
        """
        keyword = input("Keyword: ")
        return keyword

    def print_searched_keyword(self, keyword):
        """
        Print the keyword being searched for.

        :param keyword: The keyword being searched for.
        """
        print("Search keyword {}".format(keyword))

    def print_keyword_not_found(self, keyword):
        """
        Print a message indicating that a keyword was not found.

        :param keyword: The keyword that was not found.
        """
        print("Keyword {} not found".format(keyword))

    def print_ticket_invalid_id(self, case_id):
        """
        Print a message indicating that a ticket ID is invalid.

        :param case_id: The invalid ticket ID.
        """
        print("Invalid id {}: ticket not found".format(case_id))

    def print_updated_ticket(self, case_id, new_assign, new_state):
        """
        Print a message indicating that a ticket has been updated.

        :param case_id: The ID of the updated ticket.
        :param new_assign: The new assignee of the ticket.
        :param new_state: The new state of the ticket.
        """
        print(
            "Assign ticket {} to {} to state {}".format(case_id, new_assign, new_state)
        )

    def print_form_update_ticket(self):
        """
        Prompt the user to enter the details of the ticket to update.

        :return: The details of the ticket to update.
        """
        id = input("Id: ")
        state = input("State: ")
        assign_name = input("Assigned to: ")
        return id, state, assign_name

    def print_one_form_ticket(self):
        """
        Prompt the user to enter the ID of a ticket.

        :return: The ID of the ticket.
        """
        id = input("Id: ")
        return id

    def print_main_form(self):
        """
        Print the main menu of the ticket system.
        :return: The user's selection.
        """
        print("\n1. Create a ticket")
        print("2. Update a ticket")
        print("3. Close a ticket")
        print("4. Search keyword")
        print("5. Display issue")
        print("6. Get old tickets(TAR-3)")
        print("7. Sortie")

        val = input("\nEnter your selection: ")
        return val

    def print_invalid_selection(self):
        """
        Print a message indicating that the user's selection is invalid.
        """
        print("Invalid selection")

    @staticmethod
    def print_one_ticket(ticket: Ticket):
        """
        Print the details of a ticket.

        :param ticket: The ticket to print.
        """
        print("Ticket ", "id : ", ticket.id)
        print("Ticket ", "name : ", ticket.name)
        print("Ticket ", "details : ", ticket.details)
        print("Ticket ", "date : ", ticket.date)
        print("Ticket ", "state : ", ticket.state)
        print("Ticket ", "responsible : ", ticket.responsible)
        print("")
        pass

    def print_invalid_id(self):
        """
        Print an error message for an invalid ID.
        """
        print("ID is not in format Case-XXX where X represents a digit.")

    def print_invalid_name(self):
        """
        Print an error message for an invalid name.
        """
        print("Name is empty or is not alphanumeric")

    def print_invalid_details(self):
        """
        Print an error message for invalid description.
        """
        print("Description are empty, please fill all the details.")

    def print_invalid_type(self):
        """
        Print an error message for an invalid ticket type.
        """
        print("Type is not PR or IR.")

    def print_invalid_state(self, new_state):
        """
        Print an error message for an invalid state.
        :param new_state:  The new state of the ticket.
        """
        print("Invalid state {}".format(new_state))

    def print_invalid_responsible(self, new_assign):
        """
        Print an error message for an invalid assignee.
        :param new_assign: The new assignee of the ticket.
        """
        print("Invalid assign {}".format(new_assign))

    def print_id_already_exists(self):
        """
        Print an error message when the ticket ID already exists.
        """
        print("ID already exists")

    def print_tar_3_tickets(self, tickets):
        """
        Print the details of old tickets.
        :param tickets: The old tickets.
        """
        print(str(tickets.get("new").get("count")) + " old NEW tickets: ")
        for ticket in tickets.get("new").get("tickets"):
            self.print_one_ticket(ticket)
            print("-----------------------")
        print(str(tickets.get("assigned").get("count")) + " old ASSIGNED tickets: ")
        for ticket in tickets.get("assigned").get("tickets"):
            self.print_one_ticket(ticket)
            print("-----------------------")

        print(str(tickets.get("all").get("count")) + " old tickets: ")
        for ticket in tickets.get("all").get("tickets"):
            self.print_one_ticket(ticket)
            print("=======================")

    def print_search(self, keyword, tickets):
        """
        Print the details of tickets that match a keyword.

        :param keyword: The keyword that was searched for.
        :param tickets: The tickets that match the keyword.
        """
        print("Searched keyword: ", keyword)
        for ticket in tickets:
            self.print_one_ticket(ticket)
            print("-----------------------")
        print("Total tickets: ", len(tickets))
        print("=======================")
