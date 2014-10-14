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
    # def test_total_infection(self):
        # total_infection(self.users, self.graph, 1)
        # self.assertEqual([u.updated for u in self.users],
                        # [True, True, True, False, False, True, False, True, True, True])
    def test_limited_infection(self):
        limited_infection(self.users, self.graph, 5)
    #    self.assertEqual([u.updated for u in self.users],
                        # [True, True, True, False, False, False, False, False, True, True])


if __name__ == "__main__":
    unittest.main()
