from src.abstract_interface import AbstractInterface
import PySimpleGUI as sg

from src.constants import Type
from src.ticket import Ticket


class GUI(AbstractInterface):

    def __init__(self):
        self.window = sg.Window("Ticket Management System", self.get_default_layout())

    @staticmethod
    def get_default_layout():
        return [
            [sg.Text("Ticket Management System")],
            [sg.Button("Create a ticket", key="create_ticket")],
            [sg.Button("Update a ticket", key="update_ticket")],
            [sg.Button("Close a ticket", key="close_ticket")],
            [sg.Button("Search keyword", key="search_keyword")],
            [sg.Button("Display issue", key="display_issue")],
            [sg.Button("Exit", key="exit")],
        ]


    def print_close_ticket(self, case_id):
        pass

    def print_form_close_ticket(self):
        layout = [
            [sg.Text("Ticket Management System")],
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
        pass

    def print_created_ticket(self, ticket: Ticket):
        sg.popup("Ticket created: ", ticket.id)
        pass

    def print_form_create_ticket(self):
        layout = [
            [sg.Text("Ticket Management System", size=(30, 1), font=("Helvetica", 25))],
            [sg.Text("Create new ticket", size=(20, 1), font=("Helvetica", 20))],
            [sg.Text("Ticket-ID"), sg.Input(key="case_id")],
            [sg.Text("Customer name"), sg.Input(key="name")],
            [sg.Text("Case description"), sg.Input(key="description")],
            [sg.Text("Case type")],
            [sg.Radio(Type.PR.value, "type", default=True, key=Type.PR.value), sg.Radio(Type.IR.value, "type", key=Type.IR.value)],
            [
                sg.Button("Create ticket", key="Create ticket"),
                sg.Button("Cancel", key="cancel"),
            ],]
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
                if values["case_id"] == "" or values["name"] == "" or values["description"] == "":
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
        pass

    def print_ticket_invalid_id(self, case_id):
        pass

    def print_form_search_ticket(self):
        pass

    def print_searched_keyword(self, keyword):
        pass

    def print_keyword_not_found(self, keyword):
        pass

    def print_updated_ticket(self, case_id, new_assign, new_state):
        pass

    def print_form_update_ticket(self):
        pass

    def print_one_form_ticket(self):
        pass

    def print_main_form(self):
        self.window = None
        self.window = sg.Window("Ticket Management System", self.get_default_layout())

        while True:
            event, values = self.window.read()

            if event in (sg.WINDOW_CLOSED, "exit"):
                self.window.close()
                return "6"
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


    def print_invalid_selection(self):
        pass

    def print_invalid_id(self):
        pass

    def print_invalid_name(self):
        pass

    def print_invalid_details(self):
        pass

    def print_invalid_type(self):
        pass

    def print_invalid_state(self, new_state):
        pass

    def print_invalid_responsible(self, new_assign):
        pass

    def print_id_already_exists(self):
        pass
