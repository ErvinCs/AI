from src.EA.Population import Population
import matplotlib.pyplot as mpl
from copy import deepcopy
class EAUI:
    def __init__(self, fileName="Files/input1.txt", mutationRate=0.3, crossRate = 0.7, populationSize = 40, tourSize = 5, iterNo=500):
        #self.__mutationRate = self.readMutationRate()
        #self.__crossRate = self.readCrossoverRate()
        #self.__populationSize = self.readPopSize()
        #self.__tourSize = self.readTourSize()
        #self.__iterNo = self.readIterNo
        self.__mutationRate = mutationRate
        self.__crossRate = crossRate
        self.__populationSize = populationSize
        self.__tourSize = tourSize
        self.__fileName = fileName
        self.__population = Population(self.__fileName, self.__populationSize,
                                       self.__mutationRate, self.__crossRate, self.__tourSize)
        self.__iterNo = iterNo


    def readMutationRate(self):
        try:
            mutationRate = float(input("MutationRate="))
            return mutationRate
        except Exception as ex:
            print("Invalid input!")
            self.readMutationRate()

    def readCrossoverRate(self):
        try:
            crossRate = float(input("CrossoverRate="))
            return crossRate
        except Exception as ex:
            print("Invalid input!")
            self.readCrossoverRate()

    def readPopSize(self):
        try:
            popSize = int(input("PopulationSize="))
            return popSize
        except Exception as ex:
            print("Invalid input!")
            self.readPopSize()

    def readTourSize(self):
        try:
            tourSize = int(input("TournamentSize="))
            return tourSize
        except Exception as ex:
            print("Invalid input!")
            self.readTourSize()

    def readIterNo(self):
        try:
            iterNo = int(input("IterationNumber="))
            return iterNo
        except Exception as ex:
            print("Invalid input!")
            self.readIterNo()

    def run(self, show=True):
        i = 0
        mostFitList = []
        bestMostFit = self.__population.rankingSelection()
        while i < self.__iterNo:
            i += 1

            mostFit = self.__population.rankingSelection()
            if mostFit.getFitness() < bestMostFit.getFitness():
                bestMostFit = deepcopy(mostFit)
            mostFitList.append(mostFit.getFitness())

            if show is True:
                print("Generation: " + str(i))
                print("Most fit: " + str(mostFit.getFitness()) + "\n")

            if mostFit.getFitness() == 0 or i == self.__iterNo:
                i = self.__iterNo
                if show is True:
                    print(str(bestMostFit) + "\n")
                    self.statistics(mostFitList)
                return bestMostFit
            self.__population = self.__population.evolve()

    def statistics(self, list):
        mpl.plot(list)
        mpl.show()