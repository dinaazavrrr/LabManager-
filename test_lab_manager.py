import unittest
import os
from lab_manager import add_lab, list_labs, DB_FILE

class TestLabManager(unittest.TestCase):
    def setUp(self):
        if os.path.exists(DB_FILE):
            os.remove(DB_FILE)

    def test_add_and_list(self):
        add_lab("Мережі", "1", "A", "здано")
        labs = list_labs()
        self.assertEqual(len(labs), 1)
        self.assertEqual(labs[0]["name"], "Мережі")

    def test_filter_status(self):
        add_lab("ОС", "2", "B", "не здано")
        add_lab("Java", "3", "A", "здано")
        labs_done = list_labs("здано")
        self.assertEqual(len(labs_done), 1)
        self.assertEqual(labs_done[0]["name"], "Java")

if __name__ == '__main__':
    unittest.main()
