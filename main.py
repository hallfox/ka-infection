from infection import *
import unittest

class InfectionTest(unittest.TestCase):
    def setUp(self):
        self.users = [User() for x in range(11)] #a collection of users
        self.graph = {
            0: [5],
            1: [0],
            2: [6],
            3: [7],
            4: [8,9],
            5: [],
            6: [2],
            7: [],
            8: [],
            9: [],
            10: []
        }
    def test_total_infection(self):
        total_infection(self.users, self.graph, 1)
        self.assertEqual([u.updated for u in self.users],
                        [True, True, False, False, False, True, False, False, False, False, False])
    def test_basic_limited(self):
        print("---Basic limited---")
        inf = limited_infection(self.users, self.graph, 5)
        self.assertTrue(inf <= 5)
    def test_large_limit(self):
        print("---Large limit---")
        inf = limited_infection(self.users, self.graph, 100)
        self.assertTrue(inf <= 100)
    def test_limit_exception(self):
        print("---Limit exception---")
        self.assertRaises(ValueError, limited_infection, self.users, self.graph, 1)
    def test_low_limit(self):
        print("---Low limit---")
        inf = limited_infection(self.users, self.graph, 2)
        self.assertTrue(inf <= 2)

if __name__ == "__main__":
    unittest.main()
