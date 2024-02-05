import datetime


class Ticket:
    def __init__(self, id, name, details, ticket_type, state, responsible):
        self.id = id
        self.name = name
        self.details = details
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.type = ticket_type
        self.state = state
        self.responsible = responsible

    def __eq__(self, other):
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
        return (
            item == self.id
            or item == self.name
            or item == self.details
            or item == self.type
            or item == self.state
            or item == self.responsible
        )
