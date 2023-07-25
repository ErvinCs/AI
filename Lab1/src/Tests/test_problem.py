import unittest
from unittest import TestCase
from src.domain.Problem import Problem

class TestProblem(TestCase):
    def setUp(self):
        problem = Problem("test.txt")
        return problem

    def test_findSpot(self):
        p = self.setUp()
        self.assertEqual(p.findSpot(), (0,3))

    def test_heuristics(self):
        p = self.setUp()
        s1 = p.getState()
        s1.setItem(3, 1, 3)
        s2 = p.getState()
        s2.setItem(3, 1, 4)
        self.assertTrue(p.heuristics(s1, s2, 3, 1) == s1)


if __name__ == "__main__":
    testSuite = unittest.TestSuite()
    testSuite.addTest(TestProblem)
    unittest.main()
