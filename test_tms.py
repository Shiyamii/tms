import datetime
import unittest
import tms


class CreateTicketTest(unittest.TestCase):
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

    def test_same_id(self):
        tms.create_ticket(
            self.ticket["id"],
            self.ticket["name"],
            self.ticket["details"],
            self.ticket["type"],
            self.backlog,
        )
        with self.assertRaises(Exception):
            tms.create_ticket(
                self.ticket["id"],
                self.ticket["name"],
                self.ticket["details"],
                self.ticket["type"],
                self.backlog,
            )


class UpdateTicketTest(unittest.TestCase):
    def setUp(self):
        self.ticket = {
            "id": "Case-001",
            "name": "IUT",
            "type": "PR",
            "details": "IUT is not working",
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "state": tms.State.NEW.value,
            "responsible": tms.Responsible.L1.value,
        }
        self.backlog = [self.ticket]

    def test_update_ticket(self):
        success = tms.update_ticket(
            self.ticket["id"],
            tms.State.ANALYSIS.value,
            tms.Responsible.L2.value,
            self.backlog,
        )
        self.assertEqual(self.backlog[0]["state"], tms.State.ANALYSIS.value)
        self.assertEqual(self.backlog[0]["responsible"], tms.Responsible.L2.value)
        self.assertTrue(success)

    def test_wrong_state(self):
        success = tms.update_ticket(
            self.ticket["id"], "WRONG", tms.Responsible.L2.value, self.backlog
        )
        self.assertEqual(self.backlog[0]["state"], tms.State.NEW.value)
        self.assertEqual(self.backlog[0]["responsible"], tms.Responsible.L1.value)
        self.assertNotEqual(self.backlog[0]["state"], "WRONG")
        self.assertNotEqual(self.backlog[0]["responsible"], tms.Responsible.L2.value)
        self.assertFalse(success)

    def test_wrong_responsible(self):
        success = tms.update_ticket(
            self.ticket["id"], tms.State.ANALYSIS.value, "WRONG", self.backlog
        )
        self.assertEqual(self.backlog[0]["state"], tms.State.NEW.value)
        self.assertEqual(self.backlog[0]["responsible"], tms.Responsible.L1.value)
        self.assertNotEqual(self.backlog[0]["state"], tms.State.ANALYSIS.value)
        self.assertNotEqual(self.backlog[0]["responsible"], "WRONG")
        self.assertFalse(success)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(CreateTicketTest("test_default_widget_size"))
    suite.addTest(UpdateTicketTest("test_widget_resize"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
