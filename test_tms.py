import datetime
import unittest
import tms


class TestTms(unittest.TestCase):
    def setUp(self):
        self.backlog = []
        self.ticket = {
            "id": "Case-001",
            "name": "IUT",
            "type": "PR",
            "details": "IUT is not working",
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "state": tms.State.NEW.value,
            "responsible": tms.Responsible.L1.value,
        }

    def test_creation(self):
        tms.create_ticket(
            self.ticket["id"],
            self.ticket["name"],
            self.ticket["details"],
            self.ticket["type"],
            self.backlog,
        )
        self.assertEqual(self.backlog[0], self.ticket)

    def test_creation_invalid_id(self):
        with self.assertRaises(Exception):
            tms.create_ticket(
                "Case-",
                self.ticket["name"],
                self.ticket["details"],
                self.ticket["type"],
                self.backlog,
            )

    def test_creation_wrong_name_field(self):
        with self.assertRaises(Exception):
            tms.create_ticket(
                self.ticket["id"],
                "",
                self.ticket["details"],
                self.ticket["type"],
                self.backlog,
            )
        with self.assertRaises(Exception):
            tms.create_ticket(
                self.ticket["id"],
                422,
                self.ticket["details"],
                self.ticket["type"],
                self.backlog,
            )

    def test_creation_wrong_description_field(self):
        with self.assertRaises(Exception):
            tms.create_ticket(
                self.ticket["id"],
                self.ticket["name"],
                "",
                self.ticket["type"],
                self.backlog,
            )
        with self.assertRaises(Exception):
            tms.create_ticket(
                self.ticket["id"],
                self.ticket["name"],
                422,
                self.ticket["type"],
                self.backlog,
            )

    def test_creation_wrong_type_field(self):
        with self.assertRaises(Exception):
            tms.create_ticket(
                self.ticket["id"],
                self.ticket["name"],
                self.ticket["details"],
                "PRR",
                self.backlog,
            )
        with self.assertRaises(Exception):
            tms.create_ticket(
                self.ticket["id"],
                self.ticket["name"],
                self.ticket["details"],
                422,
                self.backlog,
            )


if __name__ == "__main__":
    unittest.main()
