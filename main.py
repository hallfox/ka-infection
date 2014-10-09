from infection import *
import unittest

class InfectionTest(unittest.TestCase):
    def setUp(self):
        self.users = [User(0) for x in range(10)] #a collection of users
        self.graph = {
        0: [1],
        1: [0,2,8,9],
        2: [1,5,7],
        3: [4],
        4: [3],
        5: [2],
        6: [],
        7: [2],
        8: [1],
        9: [1]
        }
    def test_total_infection(self):
        total_infection(self.users, self.graph, 1)
        self.assertEqual([u.version for u in self.users], [1, 1, 1, 0, 0, 1, 0, 1, 1, 1])


if __name__ == "__main__":
    unittest.main()
