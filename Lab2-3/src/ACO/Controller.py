from copy import deepcopy
from random import randint
from random import random
import math

from src.ACO.Ant import Ant
from src.Common.Problem import Problem

class Controller:
    def __init__(self, fileName, antPopSize, evapCoef, pheroStrCoef, distancePriorityCoef, randomCoef):
        '''
        :param fileName: file path - contains the initial population
        :param antPopSize: ant population size - integer
        :param evapCoef: pheromone evaporation speed - (0,1)
        :param pheroStrCoef: pheromone power level - >1
        :param distancePriorityCoef: ants will prioritize the closer cubes - >1
        :param randomCoef: chances of an ant to move randomly - (0,1)
        '''
        self.__fileName = fileName
        #Cubes
        self.__problem = Problem(fileName)
        self.__cubes = self.__problem.getData()
        self.__cubePopSize = len(self.__cubes)
        self.__matrix = self.__problem.getMatrix()
        #Ants
        self.__antPopSize = antPopSize
        self.__ants = []
        self.initAnts()
        self.__bestAnt = self.__ants[0]
        self.__current = 1
        #Coeficients
        self.__evaporationCoef = evapCoef
        self.__pheroStrCoef = pheroStrCoef
        self.__distancePriorityCoef = distancePriorityCoef
        self.__bossCoef = self.__pheroStrCoef * 2
        self.__randomCoef = randomCoef
        self.__trails = [[0]*(self.__cubePopSize) for i in range(0, self.__cubePopSize+1)]
        self.initPathPhero()

    def getBestAnt(self):
        return self.__bestAnt

    def reset(self):
        '''
        Reset the ant population
        '''
        self.__ants = []
        self.initAnts()
        self.__current = 1

    def initPathPhero(self):
        '''
        Set up the trails with an initial pheromone strength
        '''
        for i in range(0, self.__cubePopSize):
            for j in range(0, self.__cubePopSize):
                self.__trails[i][j] = self.__pheroStrCoef

    def initAnts(self):
        '''
        Place the ants on random initial cubes
        '''
        if (self.__antPopSize > len(self.__cubes)):
            j = 0
            for i in range(0, self.__antPopSize):
                newAnt = Ant(self.__cubes)
                newAnt.addCube(newAnt.getCubes()[j % self.__cubePopSize])
                j += 1
                self.__ants.append(newAnt)
        else:
            limit = self.__antPopSize % 4
            for i in range(0, limit):
                newAnt = Ant(self.__cubes)
                newAnt.addCube(newAnt.getCubes()[randint(0, len(self.__cubes) - 1)])
                self.__ants.append(newAnt)
            for i in range(limit, self.__antPopSize):
                newAnt = Ant(self.__cubes)
                newAnt.addCube(newAnt.getCubes()[randint(0, len(self.__cubes)-1)])
                self.__ants.append(newAnt)

    #MoveOneAnt
    def nextCube(self, ant):
        '''
        Adds a cube to Ant's path
        :param ant: Ant
        :return: Ant
        '''
        currCube = ant.getTopCube()
        #Check if the ant should visit randomly
        if random() < self.__randomCoef:
            randCube = ant.getCubes()[randint(0, len(ant.getCubes())-1)]
            added = ant.addCube(randCube)
            return added
        #Place small cubes over the bigger ones; avoid successive colors
        fitness = 4
        new = currCube
        for i in range(0, len(ant.getCubes())):
            if ant.getCubes()[i].getSize() == new.getSize() and ant.getCubes()[i].getColor() != new.getColor() and fitness >= 0\
                    and self.cubeDistance(ant.getCubes()[i], new) < self.__distancePriorityCoef:
                new = ant.getCubes()[i]
                fitness = 0
            if ant.getCubes()[i].getSize() == new.getSize() and ant.getCubes()[i].getColor() != new.getColor() and fitness >= 1:
                new = ant.getCubes()[i]
                fitness = 1
            elif currCube.getSize() < new.getSize() and currCube.getColor() != new.getColor() and fitness >= 2:
                new = ant.getCubes()[i]
                fitness = 2
            elif currCube.getSize() == new.getSize() and fitness >= 3:
                new = ant.getCubes()[i]
                fitness = 3
            elif currCube.getSize() < new.getSize() and fitness >= 4:
                new = ant.getCubes()[i]
                fitness = 4
        if new != currCube:
            added = ant.addCube(new)
            return added
        #Random
        added = ant.addCube(ant.getCubes()[randint(0, len(ant.getCubes())-1)])
        return added

    #LocalUpdate
    def move(self):
        '''
        Adds a cube to each Ant's path and updates the pheromone trails
        '''
        #For each move, the pheromones evaporate
        for i in range(0, self.__cubePopSize):
            for j in range(0, self.__cubePopSize):
                self.__trails[i][j] *= self.__evaporationCoef
        #Each ant moves to the next best Cube
        for i in range(0, self.__antPopSize):
            cube = self.nextCube(self.__ants[i])
            i, j = self.findCubeOnMatrix(cube)
            self.__trails[i][j] += self.__pheroStrCoef
        self.__current += 1

    def findCubeOnMatrix(self, cube):
        '''
        Returns the coordinates of cube on the matrix
        :param cube: Cube
        :return: (integer, integer)
        :raise: Exception - if someone messes up my code and Neo, i mean, Cubes escape the matrix
        '''
        for i in range(0, self.__cubePopSize):
            for j in range(0, self.__cubePopSize):
                if self.__matrix[i][j] == cube:
                    return (i, j)
        raise Exception("Cube escaped the matrix!")

    def cubeDistance(self, cube1, cube2):
        '''
        Returns the distance between 2 cubes on the matrix
        :param cube1: Cube
        :param cube2: Cube
        :return: Float
        '''
        c1i, c1j = self.findCubeOnMatrix(cube1)
        c2i, c2j = self.findCubeOnMatrix(cube2)
        return math.sqrt((c1i - c2i)*(c1i - c2i) + (c1j - c2j)*(c1j - c2j))


    #GlobalUpdate
    def bestAnt(self):
        '''
        Determines the best ant of a generation
        :return: ant with the best fitness
        '''
        for i in range(0, len(self.__ants)):
            if self.__ants[i].getFitness() < self.__bestAnt.getFitness():
                self.__bestAnt = self.__ants[i]
        return self.__bestAnt


    def iteration(self):
        '''
        Every iteration(generation) the ants exhaust their moves
        With each move a localUpdate of the pheromones occurs
        At the end a globalUpdate of the leader occurs
        :return: the best ant of the iteration
        '''
        while len(self.__cubes) > self.__current:
            self.move()
        best = self.bestAnt()
        return (best, self)


