from src.ACO.Controller import Controller
import matplotlib.pyplot as mpl
from copy import deepcopy

class ACOUI:
    def __init__(self, fileName="Files/input1.txt", antPopSize=30, evapCoef=0.3, pheroStrCoef=1, distancePriorityCoef=5, randomCoef=0.1, iterNo=500):
        self.__fileName = fileName
        # self.__antPopSize = self.readAntPopSize()
        # self.__evapCoef = self.readEvapCoef()
        # self.__pheroStrCoef = self.readPheroStrCoef()
        # self.__distancePriorityCoef = self.readDistancePriorityCoef()
        # self.__randomCoef = self.readRandCoef()
        # self.__iterNo = self.readIterNo()
        self.__antPopSize = antPopSize
        self.__evapCoef = evapCoef
        self.__pheroStrCoef = pheroStrCoef
        self.__distancePriorityCoef = distancePriorityCoef
        self.__randomCoef = randomCoef
        self.__iterNo = iterNo
        self.__con = Controller(self.__fileName, self.__antPopSize, self.__evapCoef,
                                self.__pheroStrCoef, self.__distancePriorityCoef, self.__randomCoef)

    def readIterNo(self):
        try:
            iterNo = int(input("IterationNumber="))
            return iterNo
        except Exception as ex:
            print("Invalid input!")
            self.readIterNo()

    def readAntPopSize(self):
        try:
            antPop = int(input("AntPopulationSize="))
            return antPop
        except Exception as ex:
            print("Invalid input!")
            self.readAntPopSize()

    def readEvapCoef(self):
        try:
            evapCoef = int(input("EvaporationCoeficient="))
            return evapCoef
        except Exception as ex:
            print("Invalid input!")
            self.readEvapCoef()

    def readPheroStrCoef(self):
        try:
            pheroStrCoef = int(input("PheromoneStrengthCoeficient="))
            return pheroStrCoef
        except Exception as ex:
            print("Invalid input!")
            self.readPheroStrCoef()

    def readDistancePriorityCoef(self):
        try:
            distCoef = int(input("DistancePriorityCoeficient=="))
            return distCoef
        except Exception as ex:
            print("Invalid input!")
            self.readDistancePriorityCoef()

    def readRandCoef(self):
        try:
            randCoef = int(input("RandomnessCoeficient="))
            return randCoef
        except Exception as ex:
            print("Invalid input!")
            self.readRandCoef()

    def run(self, show=True):
        '''
        Run the algorithm until a solution is found or the iteration limit is reached
        '''
        i = 0
        leaderList = []
        best = 0
        bestest = 0
        while i < self.__iterNo:
            i += 1

            best, self.__con = self.__con.iteration()
            if i == 1:
                best = self.__con.getBestAnt()
                bestest = deepcopy(best)
            if best.getFitness() < bestest.getFitness():
                bestest = deepcopy(best)
            leaderList.append(bestest.getFitness())

            if show is True:
                print("Generation: " + str(i))
                print("Best: " + str(best.getFitness()))
                #print(str(best) + "\n")

            if best.getFitness() == 0 or i == self.__iterNo:
                i = self.__iterNo
                if show is True:
                    print(str(bestest) + "\n")
                    self.statistics(leaderList)
                return bestest

            self.__con.reset()

    def statistics(self, list):
        mpl.plot(list)
        mpl.show()

