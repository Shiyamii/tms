from abc import ABC, abstractmethod


class DataInterface(ABC):
    @abstractmethod
    def get_tickets(self, ticket):
        pass

    @abstractmethod
    def create_ticket(self, ticket):
        pass

    @abstractmethod
    def update_ticket(self, ticket):
        pass

    @abstractmethod
    def delete_ticket(self, ticket):
        pass
