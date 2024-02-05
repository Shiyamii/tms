import unittest
from src.tms import TMS
from src.ticket import Ticket
from src.constants import State, Responsible, Type
from src.interface import Interface


class CreateTicketTest(unittest.TestCase):
    def setUp(self):
        self.tms = TMS(Interface())
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
        self.tms.create_ticket(
            self.ticket.id,
            self.ticket.name,
            self.ticket.details,
            self.ticket.type.value,
        )
        self.assertTrue(self.ticket.__eq__(self.tms.backlog[0]))

    def test_creation_invalid_id(self):
        success = self.tms.create_ticket(
            "Case-",
            self.ticket.name,
            self.ticket.details,
            self.ticket.type.value,
        )
        self.assertEqual(self.tms.backlog, [])
        self.assertFalse(success)

    def test_creation_wrong_type_field(self):
        success = self.tms.create_ticket(
            self.ticket.id,
            self.ticket.name,
            self.ticket.details,
            "PRR",
        )

        self.assertEqual(self.tms.backlog, [])
        self.assertFalse(success)
        success = self.tms.create_ticket(
            self.ticket.id,
            self.ticket.name,
            self.ticket.details,
            422,
        )

        self.assertEqual(self.tms.backlog, [])
        self.assertFalse(success)

    def test_same_id(self):
        success = self.tms.create_ticket(
            self.ticket.id,
            self.ticket.name,
            self.ticket.details,
            self.ticket.type.value,
        )
        self.assertTrue(success)
        self.assertTrue(self.ticket.__eq__(self.tms.backlog[0]))
        success = self.tms.create_ticket(
            self.ticket.id,
            self.ticket.name,
            self.ticket.details,
            self.ticket.type.value,
        )
        self.assertFalse(success)


class UpdateTicketTest(unittest.TestCase):
    def setUp(self):
        self.tms = TMS(Interface())
        self.ticket = Ticket(
            "Case-001",
            "IUT",
            "IUT is not working",
            Type.PR,
            State.NEW,
            Responsible.L1,
        )
        self.tms.backlog = [self.ticket]

    def test_update_ticket(self):
        success = self.tms.update_ticket(
            self.ticket.id,
            State.ANALYSIS.value,
            Responsible.L2.value,
        )
        self.assertEqual(self.tms.backlog[0].state, State.ANALYSIS)
        self.assertEqual(self.tms.backlog[0].responsible, Responsible.L2)
        self.assertTrue(success)

    def test_wrong_state(self):
        success = self.tms.update_ticket(self.ticket.id, "WRONG", Responsible.L2)
        self.assertEqual(self.tms.backlog[0].state, State.NEW)
        self.assertEqual(self.tms.backlog[0].responsible, Responsible.L1)
        self.assertNotEqual(self.tms.backlog[0].state, "WRONG")
        self.assertNotEqual(self.tms.backlog[0].responsible, Responsible.L2)
        self.assertFalse(success)

    def test_wrong_responsible(self):
        success = self.tms.update_ticket(self.ticket.id, State.ANALYSIS, "WRONG")
        self.assertEqual(self.tms.backlog[0].state, State.NEW)
        self.assertEqual(self.tms.backlog[0].responsible, Responsible.L1)
        self.assertNotEqual(self.tms.backlog[0].state, State.ANALYSIS)
        self.assertNotEqual(self.tms.backlog[0].responsible, "WRONG")
        self.assertFalse(success)


class CloseTicketTest(unittest.TestCase):
    def setUp(self):
        self.tms = TMS(Interface())
        self.ticket = Ticket(
            "Case-001",
            "IUT",
            "IUT is not working",
            Type.PR,
            State.NEW,
            Responsible.L1,
        )
        self.tms.backlog = [self.ticket]

    def test_close_ticket(self):
        success = self.tms.close_ticket(self.ticket.id)
        self.assertEqual(self.tms.closed_backlog[0], self.ticket)
        self.assertEqual(self.tms.backlog, [])
        self.assertTrue(success)

    def test_close_ticket_invalid_id(self):
        success = self.tms.close_ticket("Case-002")
        self.assertEqual(self.tms.closed_backlog, [])
        self.assertEqual(self.tms.backlog[0], self.ticket)
        self.assertFalse(success)

    def test_wrong_responsible(self):
        self.ticket.responsible = Responsible.L2
        success = self.tms.close_ticket(self.ticket.id)
        self.assertEqual(self.tms.closed_backlog, [])
        self.assertEqual(self.tms.backlog[0], self.ticket)
        self.assertFalse(success)


class SearchTicketTest(unittest.TestCase):
    def setUp(self):
        self.tms = TMS(Interface())
        self.ticket = Ticket(
            "Case-001",
            "IUT",
            "IUT is not working",
            Type.PR,
            State.NEW,
            Responsible.L1,
        )
        self.tms.backlog = [self.ticket]

    def test_search_ticket_by_type(self):
        found = self.tms.search_tickets(Type.PR.value)
        self.assertTrue(found)

    def test_search_ticket_by_state(self):
        found = self.tms.search_tickets(State.NEW.value)
        self.assertTrue(found)

    def test_search_ticket_by_responsible(self):
        found = self.tms.search_tickets(Responsible.L1.value)
        self.assertTrue(found)


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
