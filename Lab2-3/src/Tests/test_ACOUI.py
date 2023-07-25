import unittest
from unittest import TestCase

from src.Common.Cube import Cube
from src.ACO.Ant import Ant
from src.UI.ACOUI import ACOUI

class TestACO(TestCase):
    def test_run(self):
        antPopSize = 10
        evapCoef = 0.3
        pheroStrCoef = 1
        distancePriorityCoef = 2
        randomCoef = 0.1
        iterNo = 800

        runner = ACOUI("test.txt", antPopSize, evapCoef, pheroStrCoef, distancePriorityCoef, randomCoef, iterNo)

        cubes = []
        cubes.append(Cube(1, 1))
        cubes.append(Cube(2, 2))
        cubes.append(Cube(2, 1))
        cubes.append(Cube(3, 3))
        cubes.append(Cube(3, 1))
        cubes.append(Cube(3, 3))
        cubes.append(Cube(5, 2))

        finalAnt = Ant(cubes)
        for cube in cubes:
            finalAnt.addCube(cube)

        result = runner.run(False)
        # print("finalant=\n" + str(finalAnt))
        # print("result=\n" + str(result))
        self.assertEqual(result, finalAnt)

if __name__ == '__main__':
    testSuite = unittest.TestSuite()
    testSuite.addTest(TestACO)
    unittest.main()