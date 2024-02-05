import unittest
from src.backlog import Backlog
from src.tms import TMS
from src.ticket import Ticket
from src.constants import State, Responsible, Type
from src.interface import Interface
from unittest.mock import MagicMock, call


class CreateTicketTest(unittest.TestCase):
    def setUp(self):
        self.interface_mock = MagicMock(spec=Interface)
        self.backlog_mock = MagicMock(spec=Backlog)
        self.tms = TMS(self.interface_mock, self.backlog_mock)
        self.tms.backlog = []
        self.ticket = Ticket(
            "Case-001",
            "IUT",
            "IUT is not working",
            Type.PR,
            State.NEW,
            Responsible.L1,
        )

    def test_creation(self):
        self.backlog_mock.id_exists.return_value = False
        success = self.tms.create_ticket(
            self.ticket.id,
            self.ticket.name,
            self.ticket.details,
            self.ticket.type.value,
        )
        self.assertTrue(success)
        self.backlog_mock.create_ticket.assert_called_once_with(self.ticket)
        self.interface_mock.print_created_ticket.assert_called_once_with(self.ticket)

    def test_creation_invalid_id(self):
        success = self.tms.create_ticket(
            "Case-",
            self.ticket.name,
            self.ticket.details,
            self.ticket.type.value,
        )
        self.backlog_mock.create_ticket.assert_not_called()
        self.interface_mock.print_invalid_id.assert_called_once()
        self.assertFalse(success)

    def test_creation_wrong_type_field(self):
        success = self.tms.create_ticket(
            self.ticket.id,
            self.ticket.name,
            self.ticket.details,
            "PRR",
        )
        self.backlog_mock.create_ticket.assert_not_called()
        self.interface_mock.print_invalid_type.assert_called_once()
        self.assertFalse(success)

        success = self.tms.create_ticket(
            self.ticket.id,
            self.ticket.name,
            self.ticket.details,
            422,
        )

        self.backlog_mock.create_ticket.assert_not_called()
        expected_calls = [call(), call()]
        self.interface_mock.print_invalid_type.assert_has_calls(expected_calls)
        self.assertFalse(success)

    def test_same_id(self):
        self.backlog_mock.id_exists.return_value = True
        success = self.tms.create_ticket(
            self.ticket.id,
            self.ticket.name,
            self.ticket.details,
            self.ticket.type.value,
        )
        self.assertFalse(success)
        self.interface_mock.print_id_already_exists.assert_called_once()
        self.backlog_mock.create_ticket.assert_not_called()


class UpdateTicketTest(unittest.TestCase):
    def setUp(self):
        self.interface_mock = MagicMock(spec=Interface)
        self.backlog_mock = MagicMock(spec=Backlog)
        self.tms = TMS(self.interface_mock, self.backlog_mock)
        self.ticket = Ticket(
            "Case-001",
            "IUT",
            "IUT is not working",
            Type.PR,
            State.NEW,
            Responsible.L1,
        )
        self.backlog_mock.get_ticket.return_value = self.ticket

    def test_update_ticket(self):
        success = self.tms.update_ticket(
            self.ticket.id,
            State.ANALYSIS.value,
            Responsible.L2.value,
        )
        self.assertTrue(success)
        self.backlog_mock.update_ticket.assert_called_once_with(self.ticket)
        self.interface_mock.print_updated_ticket.assert_called_once_with(
            self.ticket.id,
            Responsible.L2.value,
            State.ANALYSIS.value,
        )

    def test_wrong_state(self):
        success = self.tms.update_ticket(self.ticket.id, "WRONG", Responsible.L2.value)
        self.assertFalse(success)
        self.interface_mock.print_invalid_state.assert_called_once_with("WRONG")
        self.backlog_mock.update_ticket.assert_not_called()

    def test_wrong_responsible(self):
        success = self.tms.update_ticket(self.ticket.id, State.ANALYSIS.value, "WRONG")
        self.assertFalse(success)
        self.interface_mock.print_invalid_responsible.assert_called_once_with("WRONG")
        self.backlog_mock.update_ticket.assert_not_called()


class CloseTicketTest(unittest.TestCase):
    def setUp(self):
        self.interface_mock = MagicMock(spec=Interface)
        self.backlog_mock = MagicMock(spec=Backlog)
        self.tms = TMS(self.interface_mock, self.backlog_mock)
        self.ticket = Ticket(
            "Case-001",
            "IUT",
            "IUT is not working",
            Type.PR,
            State.NEW,
            Responsible.L1,
        )
        self.backlog_mock.get_ticket.return_value = self.ticket

    def test_close_ticket(self):
        success = self.tms.close_ticket(self.ticket.id)
        self.assertTrue(success)
        self.backlog_mock.close_ticket.assert_called_once_with(self.ticket)
        self.interface_mock.print_close_ticket.assert_called_once_with(self.ticket.id)

    def test_close_ticket_invalid_id(self):
        self.backlog_mock.get_ticket.return_value = None
        success = self.tms.close_ticket("Case-002")
        self.assertFalse(success)
        self.interface_mock.print_ticket_invalid_id.assert_called_once_with("Case-002")
        self.backlog_mock.close_ticket.assert_not_called()

    def test_wrong_responsible(self):
        self.ticket.responsible = Responsible.L2
        self.backlog_mock.get_ticket.return_value = self.ticket
        success = self.tms.close_ticket(self.ticket.id)
        self.assertFalse(success)
        self.interface_mock.print_l1_close_ticket.assert_called_once()
        self.backlog_mock.close_ticket.assert_not_called()


class SearchTicketTest(unittest.TestCase):
    def setUp(self):
        self.interface_mock = MagicMock(spec=Interface)
        self.backlog_mock = MagicMock(spec=Backlog)
        self.tms = TMS(self.interface_mock, self.backlog_mock)
        self.ticket = Ticket(
            "Case-001",
            "IUT",
            "IUT is not working",
            Type.PR,
            State.NEW,
            Responsible.L1,
        )
        self.backlog_mock.search_tickets.return_value = [self.ticket]

    def test_search_ticket(self):
        self.backlog_mock.search_tickets.return_value = [self.ticket]
        found = self.tms.search_tickets(Type.PR.value)
        self.assertTrue(found)
        self.interface_mock.print_searched_keyword.assert_called_once_with(
            Type.PR.value
        )
        self.interface_mock.print_searched_ticket.assert_called_once_with(self.ticket)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(CreateTicketTest("test_create_ticket"))
    suite.addTest(UpdateTicketTest("test_update_ticket"))
    suite.addTest(CloseTicketTest("test_close_ticket"))
    suite.addTest(SearchTicketTest("test_search_ticket"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
