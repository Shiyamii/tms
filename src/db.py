from src.abstract_data import AbstractData


class DB(AbstractData):
    def __init__(self):
        self.tickets = []
        self.deleted_tickets = []
