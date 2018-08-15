import unittest
from unittest import TestCase

from src.Common.Cube import Cube
from src.EA.Pyramid import Pyramid
from src.UI.EAUI import EAUI

class TestEA(TestCase):
    def test_run(self):
        mutationRate = 0.3
        crossRate = 0.7
        populationSize = 40
        tourSize = 5
        iterNo = 100
        runner = EAUI("test.txt", mutationRate, crossRate, populationSize, tourSize, iterNo)

        cubes = []
        cubes.append(Cube(1, 1))
        cubes.append(Cube(2, 2))
        cubes.append(Cube(2, 1))
        cubes.append(Cube(3, 3))
        cubes.append(Cube(3, 1))
        cubes.append(Cube(3, 3))
        cubes.append(Cube(5, 2))

        self.assertEqual(runner.run(False), Pyramid(cubes))


if __name__ == '__main__':
    testSuite = unittest.TestSuite()
    testSuite.addTest(TestEA)
    unittest.main()