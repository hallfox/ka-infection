from infection import *
import unittest

class InfectionTest(unittest.TestCase):
    def setUp(self):
        self.users = [User() for x in range(10)] #a collection of users
        self.graph = {
            0: [],
            1: [0,2,8,9],
            2: [5,7],
            3: [4],
            4: [3],
            5: [],
            6: [],
            7: [],
            8: [],
            9: []
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
