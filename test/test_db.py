import datetime
import unittest
from unittest.mock import MagicMock, call

from database.database_connect import DatabaseConnect
from src.db import DB
from src.constants import State, Responsible, Type
from src.ticket import Ticket


class DBTest(unittest.TestCase):
    def setUp(self):
        self.db = DB()
        self.database_connection_mock = MagicMock(spec=DatabaseConnect)
        self.data = (
            "Case-011",
            "name",
            "details",
            Type.PR.value,
            State.ANALYSIS.value,
            Responsible.L2.value,
            datetime.datetime(2024, 2, 5, 20, 5, 59, 375458),
        )
        self.db.database_connection = self.database_connection_mock
        self.ticket = Ticket(
            "Case-011",
            "name",
            "details",
            Type.PR,
            State.ANALYSIS,
            Responsible.L2,
            datetime.datetime(2024, 2, 5, 20, 5, 59, 375458),
        )

    def test_data_to_ticket(self):
        ticket = self.db.data_to_ticket(self.data)
        self.assertEqual(ticket.id, "Case-011")
        self.assertEqual(ticket.name, "name")
        self.assertEqual(ticket.details, "details")
        self.assertEqual(ticket.type, Type.PR)
        self.assertEqual(ticket.state, State.ANALYSIS)
        self.assertEqual(ticket.responsible, Responsible.L2)
        self.assertEqual(
            ticket.date,
            datetime.datetime(2024, 2, 5, 20, 5, 59, 375458).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        )

    def test_data_to_tickets(self):
        data = [self.data, self.data]
        tickets = self.db.data_to_tickets(data)
        self.assertEqual(len(tickets), 2)
        ticket = tickets[1]
        self.assertEqual(ticket.id, "Case-011")
        self.assertEqual(ticket.name, "name")
        self.assertEqual(ticket.details, "details")
        self.assertEqual(ticket.type, Type.PR)
        self.assertEqual(ticket.state, State.ANALYSIS)
        self.assertEqual(ticket.responsible, Responsible.L2)
        self.assertEqual(
            ticket.date,
            datetime.datetime(2024, 2, 5, 20, 5, 59, 375458).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        )

    def test_search_tickets(self):
        self.database_connection_mock.fetch.return_value = [self.data]
        self.db.database_connection = self.database_connection_mock
        result = self.db.search_tickets("keyword_test")
        query = """
            SELECT t.id,t.name,t.description,t.ticket_type,t.state,t.responsible,b.date_created 
            FROM backlog b, ticket t 
            WHERE b.ticket_id = t.id 
            AND (t.id LIKE %s 
            OR t.name LIKE %s 
            OR t.description LIKE %s
            OR t.ticket_type LIKE %s
            OR t.state LIKE %s
            OR t.responsible LIKE %s)
        """
        data = (
            "%keyword_test%",
            "%keyword_test%",
            "%keyword_test%",
            "%keyword_test%",
            "%keyword_test%",
            "%keyword_test%",
        )
        self.database_connection_mock.fetch.assert_called_once_with(query, data)
        self.assertEqual(len(result), 1)

    def test_get_ticket(self):
        self.database_connection_mock.fetchone.return_value = self.data
        query = """
            SELECT t.id,t.name,t.description,t.ticket_type,t.state,t.responsible,b.date_created 
            FROM backlog b, ticket t 
            WHERE b.ticket_id = t.id 
            AND t.id = %s
        """
        data = ("Case-011",)
        result = self.db.get_ticket("Case-011")
        self.database_connection_mock.fetchone.assert_called_once_with(query, data)
        self.assertEqual(result.id, "Case-011")

    def test_get_ticket_not_found(self):
        self.database_connection_mock.fetchone.return_value = None
        query = """
            SELECT t.id,t.name,t.description,t.ticket_type,t.state,t.responsible,b.date_created 
            FROM backlog b, ticket t 
            WHERE b.ticket_id = t.id 
            AND t.id = %s
        """
        data = ("Case-011",)
        result = self.db.get_ticket("Case-011")
        self.database_connection_mock.fetchone.assert_called_once_with(query, data)
        self.assertIsNone(result)

    def test_id_exists(self):
        self.database_connection_mock.fetchone.return_value = self.data
        query = "SELECT * FROM ticket WHERE id = %s"
        data = ("Case-011",)
        result = self.db.id_exists("Case-011")
        self.database_connection_mock.fetchone.assert_called_once_with(query, data)
        self.assertTrue(result)

    def test_id_not_exists(self):
        self.database_connection_mock.fetchone.return_value = None
        query = "SELECT * FROM ticket WHERE id = %s"
        data = ("Case-011",)
        result = self.db.id_exists("Case-011")
        self.database_connection_mock.fetchone.assert_called_once_with(query, data)
        self.assertFalse(result)

    def test_create_ticket(self):
        self.db.create_ticket(self.ticket)
        query1 = """
            INSERT INTO ticket (id, name, description, ticket_type, state, responsible)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        data1 = (
            "Case-011",
            "name",
            "details",
            Type.PR.value,
            State.ANALYSIS.value,
            Responsible.L2.value,
        )
        query2 = """
            INSERT INTO backlog (date_created, ticket_id)
            VALUES (NOW(), %s);
        """
        data2 = ("Case-011",)
        calls = [call(query1, data1), call(query2, data2)]
        self.database_connection_mock.execute.assert_has_calls(calls)

    def test_update_ticket(self):
        self.database_connection_mock.fetchone.return_value = self.data
        self.db.database_connection = self.database_connection_mock
        self.db.update_ticket(self.ticket)
        query = """
            UPDATE ticket 
            SET name = %s, description = %s, ticket_type = %s, state = %s, responsible = %s
            WHERE id = %s
        """
        data = (
            "name",
            "details",
            Type.PR.value,
            State.ANALYSIS.value,
            Responsible.L2.value,
            "Case-011",
        )
        self.database_connection_mock.execute.assert_called_once_with(query, data)

    def test_update_ticket_not_found(self):
        self.database_connection_mock.fetchone.return_value = None
        self.db.database_connection = self.database_connection_mock
        result = self.db.update_ticket(self.ticket)
        self.assertFalse(result)

    def test_close_ticket(self):
        self.database_connection_mock.fetchone.return_value = self.data
        self.db.database_connection = self.database_connection_mock
        result = self.db.close_ticket(self.ticket)
        self.assertTrue(result)
        query1 = """
            UPDATE ticket 
            SET name = %s, description = %s, ticket_type = %s, state = %s, responsible = %s
            WHERE id = %s
        """
        data1 = (
            "name",
            "details",
            Type.PR.value,
            State.ANALYSIS.value,
            Responsible.L2.value,
            "Case-011",
        )
        query2 = """
            DELETE FROM backlog WHERE ticket_id = %s
        """
        data2 = ("Case-011",)
        query3 = """
            INSERT INTO deleted_backlog (date_created, ticket_id)
            VALUES (NOW(), %s);
        """
        calls = [call(query1, data1), call(query2, data2), call(query3, data2)]

        self.database_connection_mock.execute.assert_has_calls(calls)

    def test_close_ticket_not_found(self):
        self.database_connection_mock.fetchone.return_value = None
        self.db.database_connection = self.database_connection_mock
        result = self.db.close_ticket(self.ticket)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
