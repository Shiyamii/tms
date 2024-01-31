class Ticket:
    def __init__(self, id, name, details, type, state, responsible):
        self.id = id
        self.name = name
        self.details = details
        self.type = type
        self.state = state
        self.responsible = responsible

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.name == other.name
            and self.details == other.details
            and self.type == other.type
            and self.state == other.state
            and self.responsible == other.responsible
        )

    def __contains__(self, item):
        return (
            item in self.id
            or item in self.name
            or item in self.details
            or item in self.type
            or item in self.state
            or item in self.responsible
        )
