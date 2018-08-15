import random
from copy import deepcopy

from src.Common.Problem import Problem
from src.EA.Pyramid import Pyramid


class Population:
    def __init__(self, fileName, size, mutationRate, crossoverRate, tourSize, currPop=None):
        '''
        :param fileName: file path - contains the initial population
        :param size: population size - integer
        :param mutationRate: [0,1]
        :param crossoverRate: [0,1]
        :param tourSize: integer
        :param currPop: list of pyramids - list of lists of cubes
        '''
        self.__fileName = fileName
        self.__size = size
        self.__mutationRate = mutationRate
        self.__crossRate = crossoverRate
        self.__tourSize = tourSize
        self.__initPyramid = Pyramid(Problem(fileName).getData())
        if currPop is None:
            self.__currPop = self.generatePopulation()
        else:
            self.__currPop = currPop

    def getFileName(self):
        return self.__fileName

    def getSize(self):
        return self.__size

    def getMutationRate(self):
        return self.__mutationRate

    def getCrossoverRate(self):
        return self.__crossRate

    def getTourSize(self):
        return self.__tourSize

    def generatePopulation(self):
        '''
        :return: initial population
            Individuals may mutate
        '''
        population = [deepcopy(self.__initPyramid)] #list of pyramids
        for i in range(1, self.__size):
            population.append(deepcopy(self.__initPyramid.mutate(self.getMutationRate())))
        return population

    def rankingSelection(self):
        '''
        :return: the most fit individual, i.e. lowest fitness, from the current population
        '''
        best = self.__currPop[0]
        for i in range(1, len(self.__currPop)):
            if self.__currPop[i].fitness() < best.fitness():
                best = self.__currPop[i]
        return best

    def tournamentSelection(self):
        '''
        :return: the most fit individual from the tournament population
            The tournament population is selected randomly
        '''
        tournament = []
        for i in range(0, self.__tourSize):
            index = random.randint(0, self.getSize()-1)
            tournament.append(self.__currPop[index]) #list of pyramids

        tournamentPop = Population(self.getFileName(), self.getTourSize(), self.getMutationRate(), self.getCrossoverRate(), self.getTourSize(), tournament, )
        return tournamentPop.rankingSelection()

    def evolve(self):
        '''
        :return: a new, selected, generation of the population
            Keeps the best ranked individual
            Applies tournamentSelection 2 times and crossover for the winners
            The offspring of the winners may mutate
            Adds all the offsprings to the current population, sorts the resulting population and discards the lowest ranked individuals
        '''
        newPop = []
        newPop.append(self.rankingSelection())
        for i in range(1, self.getSize()):
            pyr1 = self.tournamentSelection()
            pyr2 = self.tournamentSelection()
            offspring = pyr1.crossover(pyr2, self.__crossRate)
            offspring.mutate(self.__mutationRate)
            newPop.append(offspring)
        for item in self.__currPop:
            newPop.append(item)
        newPop = self.selection(newPop)
        return Population(self.getFileName(), self.getSize(), self.getMutationRate(),
                          self.getCrossoverRate(), self.getTourSize(), newPop)

    def selection(self, population):
        '''
        :param population: array of Cubes
        :return: the best individuals from population
        '''
        for i in range(0, len(population)-1):
            for j in range(i+1, len(population)):
                if population[i].getFitness() < population[i+1].getFitness():
                    population[i], population[i+1] = population[i+1], population[i]
        return population[:self.getSize()]

    def __len__(self):
        '''
        :return: poulation size
        '''
        return self.__size

    def __getitem__(self, index):
        '''
        :param index: integer
        :return: Cube at index
        '''
        return self.__currPop[index]


