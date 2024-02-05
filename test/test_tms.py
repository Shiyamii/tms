import unittest
from src import tms
from src.ticket import Ticket
from src.constants import State, Responsible, Type


class CreateTicketTest(unittest.TestCase):
    def setUp(self):
        self.backlog = []
        self.ticket = Ticket(
            "Case-001",
            "IUT",
            "IUT is not working",
            Type.PR,
            State.NEW,
            Responsible.L1,
        )

    def test_creation(self):
        tms.create_ticket(
            self.ticket.id,
            self.ticket.name,
            self.ticket.details,
            self.ticket.type.value,
            self.backlog,
        )
        self.assertTrue(self.ticket.__eq__(self.backlog[0]))

    def test_creation_invalid_id(self):
        success = tms.create_ticket(
            "Case-",
            self.ticket.name,
            self.ticket.details,
            self.ticket.type.value,
            self.backlog,
        )
        self.assertEqual(self.backlog, [])
        self.assertFalse(success)

    def test_creation_wrong_type_field(self):
        success = tms.create_ticket(
            self.ticket.id,
            self.ticket.name,
            self.ticket.details,
            "PRR",
            self.backlog,
        )

        self.assertEqual(self.backlog, [])
        self.assertFalse(success)
        success = tms.create_ticket(
            self.ticket.id,
            self.ticket.name,
            self.ticket.details,
            422,
            self.backlog,
        )

        self.assertEqual(self.backlog, [])
        self.assertFalse(success)

    def test_same_id(self):
        success = tms.create_ticket(
            self.ticket.id,
            self.ticket.name,
            self.ticket.details,
            self.ticket.type.value,
            self.backlog,
        )
        self.assertTrue(success)
        self.assertTrue(self.ticket.__eq__(self.backlog[0]))
        success = tms.create_ticket(
            self.ticket.id,
            self.ticket.name,
            self.ticket.details,
            self.ticket.type.value,
            self.backlog,
        )
        self.assertFalse(success)


class UpdateTicketTest(unittest.TestCase):
    def setUp(self):
        self.ticket = Ticket(
            "Case-001",
            "IUT",
            "IUT is not working",
            Type.PR,
            State.NEW,
            Responsible.L1,
        )
        self.backlog = [self.ticket]

    def test_update_ticket(self):
        success = tms.update_ticket(
            self.ticket.id,
            State.ANALYSIS,
            Responsible.L2,
            self.backlog,
        )
        self.assertEqual(self.backlog[0].state, State.ANALYSIS)
        self.assertEqual(self.backlog[0].responsible, Responsible.L2)
        self.assertTrue(success)

    def test_wrong_state(self):
        success = tms.update_ticket(
            self.ticket.id, "WRONG", Responsible.L2, self.backlog
        )
        self.assertEqual(self.backlog[0].state, State.NEW)
        self.assertEqual(self.backlog[0].responsible, Responsible.L1)
        self.assertNotEqual(self.backlog[0].state, "WRONG")
        self.assertNotEqual(self.backlog[0].responsible, Responsible.L2)
        self.assertFalse(success)

    def test_wrong_responsible(self):
        success = tms.update_ticket(
            self.ticket.id, State.ANALYSIS, "WRONG", self.backlog
        )
        self.assertEqual(self.backlog[0].state, State.NEW)
        self.assertEqual(self.backlog[0].responsible, Responsible.L1)
        self.assertNotEqual(self.backlog[0].state, State.ANALYSIS)
        self.assertNotEqual(self.backlog[0].responsible, "WRONG")
        self.assertFalse(success)


class CloseTicketTest(unittest.TestCase):
    def setUp(self):
        self.ticket = Ticket(
            "Case-001",
            "IUT",
            "IUT is not working",
            Type.PR,
            State.NEW,
            Responsible.L1,
        )
        self.backlog = [self.ticket]
        self.closed_backlog = []

    def test_close_ticket(self):
        success = tms.close_ticket(self.ticket.id, self.backlog, self.closed_backlog)
        self.assertEqual(self.closed_backlog[0], self.ticket)
        self.assertEqual(self.backlog, [])
        self.assertTrue(success)

    def test_close_ticket_invalid_id(self):
        success = tms.close_ticket("Case-002", self.backlog, self.closed_backlog)
        self.assertEqual(self.closed_backlog, [])
        self.assertEqual(self.backlog[0], self.ticket)
        self.assertFalse(success)

    def test_wrong_responsible(self):
        self.ticket.responsible = Responsible.L2
        success = tms.close_ticket(self.ticket.id, self.backlog, self.closed_backlog)
        self.assertEqual(self.closed_backlog, [])
        self.assertEqual(self.backlog[0], self.ticket)
        self.assertFalse(success)


class SearchTicketTest(unittest.TestCase):
    def setUp(self):
        self.ticket = Ticket(
            "Case-001",
            "IUT",
            "IUT is not working",
            Type.PR,
            State.NEW,
            Responsible.L1,
        )
        self.backlog = [self.ticket]

    def test_search_ticket_by_type(self):
        found = tms.search_tickets(Type.PR, self.backlog)
        self.assertTrue(found)

    def test_search_ticket_by_state(self):
        found = tms.search_tickets(State.NEW, self.backlog)
        self.assertTrue(found)

    def test_search_ticket_by_responsible(self):
        found = tms.search_tickets(Responsible.L1, self.backlog)
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
