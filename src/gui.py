from src.abstract_interface import AbstractInterface
import PySimpleGUI as sg


class GUI:

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

    def run(self):
        self.window = None
        self.window = sg.Window("Ticket Management System", self.get_default_layout())

        while True:
            event, values = self.window.read()

            if event in (sg.WINDOW_CLOSED, "exit"):
                break
            elif event == "create_ticket":
                print("Creating a ticket")
            elif event == "update_ticket":
                print("Updating a ticket")
            elif event == "close_ticket":
                print("Closing a ticket")
                result = self.print_form_close_ticket()
                print("Close ticket", result)
                self.window = sg.Window(
                    "Ticket Management System", self.get_default_layout()
                )
            elif event == "search_keyword":
                print("Searching keyword")
            elif event == "display_issue":
                print("Displaying issue")

        self.window.close()

    @staticmethod
    def print_form_close_ticket():
        layout = [
            [sg.Text("Ticket Management System")],
            [sg.Text("Ticket-ID"), sg.Input(key="case_id")],
            [
                sg.Button("Close ticket", key="Close ticket"),
                sg.Button("Cancel", key="cancel"),
            ],
        ]
        window = sg.Window("Ticket Management System", layout)
        value = None
        running = True
        while running:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "cancel"):
                running = False
            elif event == "Close ticket":
                value = values["case_id"]
                running = False
        window.close()
        return value

    def button_go(self):
        sg.popup("Go button clicked", "Input value:", self.values["-IN-"])
