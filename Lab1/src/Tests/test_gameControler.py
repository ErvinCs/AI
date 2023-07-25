import unittest
from unittest import TestCase
from src.domain.State import State
from src.controller.GameController import GameControler

class TestGameControler(TestCase):
    def setUp(self):
        gc = GameControler("test.txt")
        sol = State(4, [[1, 2, 4, 3], [3, 4, 2, 1], [4, 1, 3 ,2], [2, 3, 1, 4]])
        return (gc, sol)

    def test_BFS(self):
        gc, sol = self.setUp()
        self.assertEqual(gc.BFS().getBoard(), sol.getBoard())

    def test_GBFS(self):
        gc, sol = self.setUp()
        self.assertEqual(gc.GBFS().getBoard(), sol.getBoard())

if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(TestGameControler)
    unittest.main()