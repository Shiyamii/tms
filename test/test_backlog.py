import datetime
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

    def test_get_old_new_ticket(self):
        current_datetime = datetime.datetime.now()
        three_days_ago = current_datetime - datetime.timedelta(days=4)
        formatted_result = three_days_ago.strftime("%Y-%m-%d %H:%M:%S")
        self.backlog.tickets = self.tickets
        self.tickets[0].date = formatted_result
        self.tickets[1].state = State.ANALYSIS
        self.tickets[1].date = formatted_result
        tickets = self.backlog.get_old_new_ticket()
        self.assertEqual(tickets, [self.tickets[0]])
        self.tickets[1].date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(tickets, [self.tickets[0]])

    def test_get_old_assigned_ticket(self):
        current_datetime = datetime.datetime.now()
        ten_days_ago = current_datetime - datetime.timedelta(days=11)
        formatted_result = ten_days_ago.strftime("%Y-%m-%d %H:%M:%S")
        self.backlog.tickets = self.tickets
        self.tickets[0].date = formatted_result
        self.tickets[0].state = State.ASSIGNED
        self.tickets[1].date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tickets[1].state = State.ASSIGNED
        tickets = self.backlog.get_old_assigned_ticket()
        self.assertEqual(tickets, [self.tickets[0]])

    def get_old_ticket_list(self):
        current_datetime = datetime.datetime.now()
        twenty_days_ago = current_datetime - datetime.timedelta(days=21)
        formatted_result = twenty_days_ago.strftime("%Y-%m-%d %H:%M:%S")
        self.backlog.tickets = self.tickets
        self.tickets[0].date = formatted_result
        self.tickets[1].date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tickets = self.backlog.get_old_ticket_list()
        self.assertEqual(tickets, [self.tickets[0]])


if __name__ == "__main__":
    unittest.main()
