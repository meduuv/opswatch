import unittest

from opswatch import status


class OpsWatchTests(unittest.TestCase):
    def test_status(self):
        self.assertEqual(
            status({"cpu": 80, "ram": 20}, {"cpu": 75, "ram": 50}),
            {"cpu": "alert", "ram": "ok"},
        )

    def test_unknown_metric(self):
        self.assertEqual(status({"disk": 10}, {}), {"disk": "unknown"})


if __name__ == "__main__":
    unittest.main()
