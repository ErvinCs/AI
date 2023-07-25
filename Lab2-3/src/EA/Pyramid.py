import random
from copy import deepcopy

from src.Common.Cube import Cube

class Pyramid:
    def __init__(self, cubes):
        '''
        :param cubes: list of cubes - form the pyramid
        size - length of cubes
        fitness - rank of the pyramid; the lower the better
        '''
        self.__cubes = cubes
        self.__size = len(cubes)
        self.__fitness = 0
        self.fitness()

    def getFitness(self):
        return self.__fitness

    def getSize(self):
        return self.__size

    def getCube(self, index):
        return self.__cubes[index]

    def getCubes(self):
        return self.__cubes

    def setCube(self, index, cube):
        self.__cubes[index] = cube


    def fitness(self):
        '''
        Higher with the number of incorrect cubes
        :return: integer - self fitness
        '''
        for i in range(1, self.getSize()):
            if self.__cubes[i-1].getSize() > self.__cubes[i].getSize():
                self.__fitness += 1
            if self.__cubes[i-1].getColor() == self.__cubes[i].getColor():
                self.__fitness += 1
        return self.__fitness

    def crossover(self, pyramid, crossProbability):
        '''
        :param pyramid: to crossover with self
        :param crossProbability: [0,1]
        :return: Pyramid - crossover result or the pyramid with better fitness - depends on crossProbability
            Order crossover - selects a random block of genes from self and keeps it in the offspring
                              removes the kept genes from pyramid
                              pastes the remaining genes from pyramid in the offspring
        '''
        if random.random() < crossProbability:
            newPyramid = Pyramid(deepcopy(self.__cubes))
            for i in range(0, len(self.__cubes)):
                newPyramid.setCube(i, Cube(-1, -1))

            c = deepcopy(self.__cubes)

            #Recombination: Order corssover
            pos1 = random.randint(0, pyramid.getSize()-1)
            pos2 = random.randint(0, self.getSize()-1)
            while pos1 >= pos2:
                pos1 = random.randint(0, pyramid.getSize()-1)
                pos2 = random.randint(0, self.getSize()-1)

            #Put gene block from c
            for i in range(pos1, pos2+1):
                newPyramid.setCube(i, self.getCube(i))
                c.remove(self.getCube(i))
            #Put gene block from pyramid
            for i in range(0, pos1):
                newCube = c[0]
                c.pop(0)
                newPyramid.setCube(i, newCube)
            for i in range(pos2+1, self.getSize()):
                newCube = c[0]
                c.pop(0)
                newPyramid.setCube(i, newCube)

            return newPyramid

        if self.getFitness() < pyramid.getFitness():
            return self
        return pyramid


    def mutate(self, mutationProbability):
        '''
        :param mutationProbability: [0,1]
        :return: self
            Mutate self by swapping 2 cubes - depends on mutationProbability
        '''
        if random.random() < mutationProbability:
            i1 = random.randint(0, self.getSize()-1)
            i2 = random.randint(0, self.getSize()-1)

            c1 = deepcopy(self.getCube(i1))
            c2 = deepcopy(self.getCube(i2))
            c1, c2 = c2, c1

            self.setCube(i1, c1)
            self.setCube(i2, c2)
        return self

    def __str__(self):
        '''
        :return: string representation of the list of cubes as a pyramid
        '''
        string = ""
        for cube in self.__cubes:
            string += str(cube) + "\n"
        return string

    def __eq__(self, other):
        '''
        :param other: Pyramid
        :return: True if the pyramids are identical; False otherwise
        '''
        return (self.getCubes() == other.getCubes())

    def __ne__(self, other):
        '''
        :param other: Pyramid
        :return: True if the pyramids are identical; False otherwise
        '''
        return (self.getCubes() != other.getCubes())
