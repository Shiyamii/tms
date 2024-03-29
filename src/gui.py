from src.abstract_interface import AbstractInterface
import PySimpleGUI as sg

from src.constants import Type, State, Responsible
from src.ticket import Ticket


class GUI(AbstractInterface):
    """
    This class represents the graphical user interface (GUI) for the Ticket Management System.
    It provides methods for displaying various forms and messages to the user.
    """

    def __init__(self):
        """
        Initialize the GUI with a default layout.
        """
        self.window = sg.Window("Ticket Management System", self.get_default_layout())

    @staticmethod
    def get_default_layout():
        """
        Returns the default layout for the GUI.
        """
        return [
            [sg.Text("Ticket Management System", size=(30, 1), font=("Helvetica", 25))],
            [sg.Text("Choose an action", size=(20, 1), font=("Helvetica", 20))],
            [sg.Button("Create a ticket", key="create_ticket")],
            [sg.Button("Update a ticket", key="update_ticket")],
            [sg.Button("Close a ticket", key="close_ticket")],
            [sg.Button("Search keyword", key="search_keyword")],
            [sg.Button("Display issue", key="display_issue")],
            [sg.Button("Get old ticket (TAR-3)", key="get_tar-3")],
            [sg.Button("Exit", key="exit")],
        ]

    def print_close_ticket(self, case_id):
        """
        Display a message indicating that a ticket has been closed.

        :param case_id: The ID of the closed ticket.
        """
        sg.popup("Close ticket {}".format(case_id))

    def print_form_close_ticket(self):
        """
        Display a form for closing a ticket and return the ID of the ticket to be closed.
        """
        layout = [
            [sg.Text("Ticket Management System", size=(30, 1), font=("Helvetica", 25))],
            [sg.Text("Close new ticket", size=(20, 1), font=("Helvetica", 20))],
            [sg.Text("Ticket-ID"), sg.Input(key="case_id")],
            [
                sg.Button("Close ticket", key="Close ticket"),
                sg.Button("Cancel", key="cancel"),
            ],
        ]
        self.window = sg.Window("Ticket Management System", layout)
        value = None
        running = True
        while running:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, "cancel"):
                running = False
            elif event == "Close ticket":
                value = values["case_id"]
                if value == "":
                    value = None
                    sg.popup("Please enter a Ticket-ID")
                else:
                    running = False
        self.window.close()
        return value

    def print_l1_close_ticket(self):
        """
        Display a message indicating that only L1 can close the ticket.
        """
        sg.popup("Only L1 can close the ticket")

    def print_created_ticket(self, ticket: Ticket):
        """
        Display a message indicating that a ticket has been created.

        :param ticket: The created ticket.
        """
        sg.popup("Ticket created: ", ticket.id)
        pass

    def print_form_create_ticket(self):
        """
        Display a form for creating a ticket and return the details of the ticket to be created.
        """
        layout = [
            [sg.Text("Ticket Management System", size=(30, 1), font=("Helvetica", 25))],
            [sg.Text("Create new ticket", size=(20, 1), font=("Helvetica", 20))],
            [sg.Text("Ticket-ID"), sg.Input(key="case_id")],
            [sg.Text("Customer name"), sg.Input(key="name")],
            [sg.Text("Case description"), sg.Input(key="description")],
            [sg.Text("Case type")],
            [
                sg.Radio(Type.PR.value, "type", default=True, key=Type.PR.value),
                sg.Radio(Type.IR.value, "type", key=Type.IR.value),
            ],
            [
                sg.Button("Create ticket", key="Create ticket"),
                sg.Button("Cancel", key="cancel"),
            ],
        ]
        self.window = sg.Window("Ticket Management System", layout)
        case_id = None
        name = None
        description = None
        ticket_type = None
        running = True
        while running:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, "cancel"):
                running = False
            elif event == "Create ticket":
                if (
                    values["case_id"] == ""
                    or values["name"] == ""
                    or values["description"] == ""
                ):
                    sg.popup("Please fill all fields")
                else:
                    running = False
                    case_id = values["case_id"]
                    name = values["name"]
                    description = values["description"]
                    if values[Type.IR.value]:
                        ticket_type = Type.IR.value
                    else:
                        ticket_type = Type.PR.value

        self.window.close()
        return case_id, name, description, ticket_type

    def print_searched_ticket(self, ticket: Ticket):
        """
        Display the details of a searched ticket.

        :param ticket: The searched ticket.
        """
        self.print_one_ticket(ticket)

    def print_ticket_invalid_id(self, case_id):
        """
        Display a message indicating that a ticket ID is invalid.

        :param case_id: The invalid ticket ID.
        """
        sg.popup("Invalid id {}: ticket not found".format(case_id))

    def print_form_search_ticket(self):
        """
        Display a form for searching a ticket and return the keyword to be searched.
        """
        layout = [
            [sg.Text("Ticket Management System", size=(30, 1), font=("Helvetica", 25))],
            [sg.Text("Search issue", size=(20, 1), font=("Helvetica", 20))],
            [sg.Text("Keyword"), sg.Input(key="keyword")],
            [
                sg.Button("Search ticket", key="Search ticket"),
                sg.Button("Cancel", key="cancel"),
            ],
        ]
        self.window = sg.Window("Ticket Management System", layout)
        keyword = None
        running = True
        while running:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, "cancel"):
                running = False
            elif event == "Search ticket":
                keyword = values["keyword"]
                if keyword == "":
                    keyword = None
                    sg.popup("Please enter a keyword")
                else:
                    running = False
        self.window.close()
        return keyword

    def print_searched_keyword(self, keyword):
        """
        Display a message indicating that a keyword has been searched.

        :param keyword: The searched keyword.
        """
        sg.popup("Search keyword {}".format(keyword))

    def print_keyword_not_found(self, keyword):
        """
        Display a message indicating that a keyword was not found.

        :param keyword: The keyword that was not found.
        """
        sg.popup("Keyword {} not found".format(keyword))

    def print_updated_ticket(self, case_id, new_assign, new_state):
        """
        Display a message indicating that a ticket has been updated.

        :param case_id: The ID of the updated ticket.
        :param new_assign: The new assignee of the ticket.
        :param new_state: The new state of the ticket.
        """
        sg.popup(
            "Assign ticket {} to {} to state {}".format(case_id, new_assign, new_state)
        )

    def print_form_update_ticket(self):
        """
        Display a form for updating a ticket and return the details of the ticket to be updated.
        """
        layout = [
            [sg.Text("Ticket Management System", size=(30, 1), font=("Helvetica", 25))],
            [sg.Text("Update ticket", size=(20, 1), font=("Helvetica", 20))],
            [sg.Text("Ticket-ID"), sg.Input(key="case_id")],
            [sg.Text("State")],
            [
                sg.Radio("Assigned", "state", key="assigned", default=True),
                sg.Radio("Analysis", "state", key="analysis"),
                sg.Radio("Solved", "state", key="solved"),
                sg.Radio("In delivery", "state", key="in delivery"),
            ],
            [sg.Text("Assigned to")],
            [
                sg.Radio("L1", "assign", key="L1", default=True),
                sg.Radio("L2", "assign", key="L2"),
                sg.Radio("L3", "assign", key="L3"),
            ],
            [
                sg.Button("Update ticket", key="Update ticket"),
                sg.Button("Cancel", key="cancel"),
            ],
        ]
        self.window = sg.Window("Ticket Management System", layout)
        case_id = None
        state = None
        assign_name = None
        running = True
        while running:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, "cancel"):
                running = False
            elif event == "Update ticket":
                if values["case_id"] == "":
                    sg.popup("Please fill all fields")
                else:
                    running = False
                    case_id = values["case_id"]
                    if values["analysis"]:
                        state = State.ANALYSIS.value
                    elif values["solved"]:
                        state = State.SOLVED.value
                    elif values["in delivery"]:
                        state = State.IN_DELIVERY.value
                    elif values["assigned"]:
                        state = State.ASSIGNED.value
                    if values["L1"]:
                        assign_name = Responsible.L1.value
                    elif values["L2"]:
                        assign_name = Responsible.L2.value
                    elif values["L3"]:
                        assign_name = Responsible.L3.value
        self.window.close()
        return case_id, state, assign_name

    def print_one_form_ticket(self):
        """
        Display a form for viewing a single ticket and return the ID of the ticket to be viewed.
        """
        layout = [
            [sg.Text("Ticket Management System", size=(30, 1), font=("Helvetica", 25))],
            [sg.Text("Display issue", size=(20, 1), font=("Helvetica", 20))],
            [sg.Text("Ticket-ID"), sg.Input(key="case_id")],
            [
                sg.Button("Display ticket", key="Display ticket"),
                sg.Button("Cancel", key="cancel"),
            ],
        ]
        self.window = sg.Window("Ticket Management System", layout)
        value = None
        running = True
        while running:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, "cancel"):
                running = False
            elif event == "Display ticket":
                value = values["case_id"]
                if value == "":
                    value = None
                    sg.popup("Please enter a Ticket-ID")
                else:
                    running = False
        self.window.close()
        return value

    def print_main_form(self):
        """
        Display the main form of the GUI and return the action selected by the user.
        """
        self.window = None
        self.window = sg.Window("Ticket Management System", self.get_default_layout())

        while True:
            event, values = self.window.read()

            if event in (sg.WINDOW_CLOSED, "exit"):
                self.window.close()
                return "7"
            elif event == "create_ticket":
                self.window.close()
                return "1"
            elif event == "update_ticket":
                self.window.close()
                return "2"
            elif event == "close_ticket":
                self.window.close()
                return "3"
            elif event == "search_keyword":
                self.window.close()
                return "4"
            elif event == "display_issue":
                self.window.close()
                return "5"
            elif event == "get_tar-3":
                self.window.close()
                return "6"

    def print_invalid_selection(self):
        """
        Display a message indicating that an invalid selection has been made.
        """
        sg.popup("Invalid selection")

    def print_one_ticket(self, ticket: Ticket):
        """
        Display the details of a single ticket.

        :param ticket: The ticket to be displayed.
        """
        layout = [
            [sg.Text("Ticket Management System", size=(30, 1), font=("Helvetica", 25))],
            [sg.Text("Display issue", size=(20, 1), font=("Helvetica", 20))],
            [sg.Text("Ticket-ID: "), sg.Text(ticket.id)],
            [sg.Text("Customer name: "), sg.Text(ticket.name)],
            [sg.Text("Case description: "), sg.Text(ticket.details)],
            [sg.Text("Case type: "), sg.Text(ticket.type.value)],
            [sg.Text("State: "), sg.Text(ticket.state.value)],
            [sg.Text("Responsible: "), sg.Text(ticket.responsible.value)],
            [sg.Text("Date created: "), sg.Text(ticket.date)],
            [sg.Button("Close", key="close")],
        ]

        self.window = sg.Window("Ticket Management System", layout)
        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, "close"):
                self.window.close()
                break

    def print_invalid_id(self):
        """
        Display a message indicating that a ticket ID is invalid.
        """
        sg.popup("ID is not in format Case-XXX where X represents a digit.")

    def print_invalid_name(self):
        """
        Display a message indicating that a name is invalid.
        """
        sg.popup("Name is empty or is not alphanumeric")

    def print_invalid_details(self):
        """
        Display a message indicating that the details of a ticket are invalid.
        """
        sg.popup("Description are empty, please fill all the details.")

    def print_invalid_type(self):
        """
        Display a message indicating that a ticket type is invalid.
        """
        sg.popup("Type is not PR or IR.")

    def print_invalid_state(self, new_state):
        """
        Display a message indicating that the state is invalid.

        :param new_state: The invalid state.
        """
        sg.popup("Invalid state {}".format(new_state))

    def print_invalid_responsible(self, new_assign):
        """
        Display a message indicating that an assignee is invalid.

        :param new_assign: The invalid assignee.
        """
        sg.popup("Invalid assign {}".format(new_assign))

    def print_id_already_exists(self):
        """
        Display a message indicating that a ticket ID already exists.
        """
        sg.popup("ID already exists")

    def print_tar_3_tickets(self, tickets):
        """
        Display the details of old tickets. (TAR-3)

        :param tickets: The old tickets to be displayed.
        """
        layout = [
            [sg.Text("Ticket Management System", size=(30, 1), font=("Helvetica", 25))],
            [sg.Text("Old tickets(TAR-3)", size=(20, 1), font=("Helvetica", 20))],
            [
                sg.Text("New tickets: "),
                sg.Text(tickets["new"]["count"]),
                sg.Button(
                    "View tickets",
                    key="view_new_tickets",
                    disabled=tickets["new"]["count"] == 0,
                ),
            ],
            [
                sg.Text("Assigned tickets: "),
                sg.Text(tickets["assigned"]["count"]),
                sg.Button(
                    "View tickets",
                    key="view_assigned_tickets",
                    disabled=tickets["assigned"]["count"] == 0,
                ),
            ],
            [
                sg.Text("All tickets: "),
                sg.Text(tickets["all"]["count"]),
                sg.Button(
                    "View tickets",
                    key="view_all_tickets",
                    disabled=tickets["all"]["count"] == 0,
                ),
            ],
            [sg.Button("Close", key="close")],
        ]

        self.window = sg.Window("Ticket Management System", layout)
        running = True
        while running:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, "close"):
                running = False
            elif event == "view_new_tickets":
                self.print_ticket_list(tickets["new"]["tickets"])
                pass
            elif event == "view_assigned_tickets":
                self.print_ticket_list(tickets["assigned"]["tickets"])
                pass
            elif event == "view_all_tickets":
                self.print_ticket_list(tickets["all"]["tickets"])
                pass

        self.window.close()

    @staticmethod
    def print_ticket_list(tickets, keyword=None):
        """
        Display a list of tickets.

        :param tickets: The tickets to be displayed.
        :param keyword: The keyword used to search the tickets (optional).
        """
        current_ticket = 0
        layout = [
            [sg.Text("Ticket Management System", size=(30, 1), font=("Helvetica", 25))],
            [
                sg.Text(
                    ("Tickets" if keyword is None else "Searched keyword: " + keyword),
                    size=(20, 1),
                    font=("Helvetica", 20),
                )
            ],
            [sg.Text("Ticket-ID: "), sg.Text(tickets[current_ticket].id)],
            [sg.Text("Customer name: "), sg.Text(tickets[current_ticket].name)],
            [sg.Text("Case description: "), sg.Text(tickets[current_ticket].details)],
            [sg.Text("Case type: "), sg.Text(tickets[current_ticket].type.value)],
            [sg.Text("State: "), sg.Text(tickets[current_ticket].state.value)],
            [
                sg.Text("Responsible: "),
                sg.Text(tickets[current_ticket].responsible.value),
            ],
            [sg.Text("Date created: "), sg.Text(tickets[current_ticket].date)],
            [
                sg.Button("Previous", key="previous", disabled=current_ticket == 0),
                sg.Button(
                    "Next", key="next", disabled=current_ticket == len(tickets) - 1
                ),
            ],
            [sg.Button("Close", key="close")],
        ]

        window = sg.Window("Ticket Management System", layout)
        running = True
        while running:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "close"):
                running = False
            elif event == "previous":
                if current_ticket > 0:
                    current_ticket -= 1
            elif event == "next":
                if current_ticket < len(tickets) - 1:
                    current_ticket += 1

        window.close()

    def print_search(self, keyword, tickets):
        """
        Display the results of a ticket search.

        :param keyword: The keyword used to search the tickets.
        :param tickets: The tickets found in the search.
        """
        self.print_ticket_list(tickets, keyword)
        pass
