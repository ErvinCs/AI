import unittest
from unittest import TestCase
from src.domain.State import State

class TestState(TestCase):
    def setUp(self):
        board1 = [[1, 2, 4, 0],
                  [3, 0, 0, 1],
                  [0, 1, 3, 2],
                  [2, 0, 0, 0]]
        board2 = [[1, 2, 4, 3],
                  [3, 4, 2, 1],
                  [4, 1, 3, 2],
                  [2, 3, 1, 4]]
        board3 = [[1, 2, 4, 3],
                  [3, 1, 2, 1],
                  [4, 3, 3, 2],
                  [2, 4, 1, 4]]
        board4 = [[8, 6, 7, 9, 3, 5, 4, 1, 2],
                  [3, 4, 5, 2, 1, 6, 9, 8, 7],
                  [9, 2, 1, 8, 7, 4, 6, 5, 3],
                  [7, 3, 4, 1, 5, 9, 8, 2, 6],
                  [5, 9, 2, 7, 6, 8, 1, 3, 4],
                  [1, 8, 6, 3, 4, 2, 5, 7, 9],
                  [4, 5, 3, 6, 2, 1, 7, 9, 8],
                  [2, 1, 8, 4, 9, 7, 3, 6, 5],
                  [6, 7, 9, 5, 8, 3, 2, 4, 1]]
        states = []
        states.append(State(4, board1))
        states.append(State(4, board2))
        states.append(State(4, board3))
        states.append(State(9, board4))
        return states

    def test_isExhausted(self):
        s = self.setUp()
        self.assertTrue(s[1].isExhausted())
        self.assertTrue(s[3].isExhausted())

    def test_isSolution(self):
        s = self.setUp()
        self.assertFalse(s[0].isSolution())
        self.assertTrue(s[1].isSolution())
        self.assertFalse(s[2].isSolution())
        self.assertTrue(s[3].isSolution())

if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(TestState)
    unittest.main()