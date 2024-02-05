import unittest
from src.backlog import Backlog
from src.ticket import Ticket
from src.constants import State, Responsible, Type


class BacklogTest(unittest.TestCase):
    def setUp(self):
        self.backlog = Backlog()
        self.tickets = [
            Ticket(
                "Case-001",
                "IUT",
                "IUT is not working",
                Type.PR,
                State.NEW,
                Responsible.L1,
            ),
            Ticket(
                "Case-002",
                "Test",
                "Test is not working",
                Type.IR,
                State.NEW,
                Responsible.L2,
            ),
        ]

    def test_create_ticket(self):
        success = self.backlog.create_ticket(self.tickets[0])
        self.assertEqual(self.backlog.tickets, [self.tickets[0]])
        self.assertTrue(success)

    def test_create_ticket_id_exists(self):
        self.backlog.tickets = [self.tickets[0]]
        success = self.backlog.create_ticket(self.tickets[0])
        self.assertFalse(success)

    def test_get_ticket(self):
        self.backlog.tickets = self.tickets
        ticket = self.backlog.get_ticket("Case-001")
        self.assertEqual(ticket, self.tickets[0])

    def test_get_ticket_not_found(self):
        self.backlog.tickets = self.tickets
        ticket = self.backlog.get_ticket("Case-003")
        self.assertIsNone(ticket)

    def test_id_exists(self):
        self.backlog.tickets = self.tickets
        self.assertTrue(self.backlog.id_exists("Case-001"))

    def test_id_not_exists(self):
        self.backlog.tickets = self.tickets
        self.assertFalse(self.backlog.id_exists("Case-003"))

    def test_update_ticket(self):
        self.backlog.tickets = self.tickets
        ticket = Ticket(
            "Case-001",
            "IUT",
            "IUT is not working",
            Type.PR,
            State.ANALYSIS,
            Responsible.L2,
        )
        success = self.backlog.update_ticket(ticket)
        self.assertTrue(success)
        self.assertEqual(self.backlog.tickets[0].state, State.ANALYSIS)
        self.assertEqual(self.backlog.tickets[0].responsible, Responsible.L2)

    def test_update_ticket_not_found(self):
        self.backlog.tickets = self.tickets
        ticket = Ticket(
            "Case-003",
            "IUT",
            "IUT is not working",
            Type.PR,
            State.ANALYSIS,
            Responsible.L2,
        )
        success = self.backlog.update_ticket(ticket)
        self.assertFalse(success)

    def test_close_ticket(self):
        self.backlog.tickets = [self.tickets[0], self.tickets[1]]
        self.tickets[0].state = State.CLOSED
        success = self.backlog.close_ticket(self.tickets[0])
        self.assertTrue(success)
        self.assertEqual(self.backlog.deleted_tickets, [self.tickets[0]])
        self.assertEqual(self.backlog.tickets, [self.tickets[1]])

    def test_close_ticket_not_found(self):
        self.backlog.tickets = self.tickets
        ticket = Ticket(
            "Case-003",
            "IUT",
            "IUT is not working",
            Type.PR,
            State.CLOSED,
            Responsible.L1,
        )
        success = self.backlog.close_ticket(ticket)
        self.assertFalse(success)


if __name__ == "__main__":
    unittest.main()
