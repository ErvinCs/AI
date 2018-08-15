import unittest
from unittest import TestCase
from src.Tests.test_gameControler import TestGameControler
from src.Tests.test_problem import TestProblem
from src.Tests.test_state import TestState

if __name__ == '__main__':
    testSuite = unittest.TestSuite()
    testSuite.addTest(TestGameControler)
    testSuite.addTest(TestProblem)
    testSuite.addTest(TestState)
    unittest.main()