from abc import ABC, abstractmethod
from typing import Optional
from src.ticket import Ticket


class AbstractData(ABC):
    @abstractmethod
    def search_tickets(self, keyword) -> list[Ticket]:
        pass

    @abstractmethod
    def get_ticket(self, ticket_id) -> Optional[Ticket]:
        pass

    @abstractmethod
    def id_exists(self, ticket_id) -> bool:
        pass

    @abstractmethod
    def create_ticket(self, ticket) -> bool:
        pass

    @abstractmethod
    def update_ticket(self, ticket) -> bool:
        pass

    @abstractmethod
    def close_ticket(self, ticket) -> bool:
        pass
