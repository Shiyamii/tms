import datetime


class Ticket:
    """
    A class to represent a Ticket.
    """

    def __init__(self, id, name, details, ticket_type, state, responsible, date=None):
        """
        Construct a new Ticket object.

        :param id: The ID of the ticket.
        :param name: The name of the ticket.
        :param details: The details of the ticket.
        :param ticket_type: The type of the ticket.
        :param state: The state of the ticket.
        :param responsible: The responsible person for the ticket.
        :param date: The date the ticket was created.
        """
        self.id = id
        self.name = name
        self.details = details
        if date:
            self.date = date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.type = ticket_type
        self.state = state
        self.responsible = responsible

    def get_age(self):
        """
        Get the age of the ticket.

        :return: The age of the ticket in timestamp.
        """
        return datetime.datetime.now() - datetime.datetime.strptime(
            self.date, "%Y-%m-%d %H:%M:%S"
        )

    def __eq__(self, other):
        """
        Check if two tickets are equal.

        :param other: The other ticket to compare.
        :return:  True if the tickets are equal, False otherwise.
        """
        return (
            self.id == other.id
            and self.name == other.name
            and self.details == other.details
            and self.date == other.date
            and self.type == other.type
            and self.state == other.state
            and self.responsible == other.responsible
        )

    def __contains__(self, item):
        """
        Check if an item is in the ticket.
        :param item: The item to check.
        :return: True if the item is in the ticket, False otherwise.
        """
        return (
            item == self.id
            or item == self.name
            or item == self.details
            or item == self.type
            or item == self.state
            or item == self.responsible
        )

    def __str__(self):
        """
        Return the string representation of the ticket.
        :return: The string representation of the ticket.
        """
        return f"Ticket id: {self.id}, name: {self.name}, details: {self.details}, date: {self.date}, type: {self.type}, state: {self.state}, responsible: {self.responsible}"
