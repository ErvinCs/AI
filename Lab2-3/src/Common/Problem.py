from src.Common.Cube import Cube
from random import randint

class Problem:
    def __init__(self, fileName):
        '''
        :param fileName: file path - contains the initial population
        '''
        self.__fileName = fileName.strip()
        self.__initCubes = self.loadData()
        self.__matrix = self.arrayToMatrix()
        #self.printTest()

    def getFileName(self):
        return self.__fileName

    def getData(self):
        '''
        :return: initial list of Cube i.e. the file's contents
        '''
        return self.__initCubes

    def getMatrix(self):
        '''
        :return: initial matrix from the list of Cubes
        '''
        return self.__matrix

    def loadData(self):
        '''
        Reads the Cubes from a text file: Cube(size, color)
        :return: list of Cube
        '''
        f = open(self.__fileName, "r")
        f.readline()
        cubes = []
        lines = f.readlines()
        for line in lines:
            line.strip()
            line = line.split()
            cubes.append(Cube(int(line[0]), int(line[1])))
        cubes = sorted(cubes, key=lambda cube: cube.getSize())
        f.close()
        return cubes

    def arrayToMatrix(self):
        '''
        Creates a matrix from the list of Cubes
        :return: matrix of Cube
        '''
        size = len(self.__initCubes)
        matrix = [[Cube(-1, -1)]*size for i in range(0, size)]
        for c in self.__initCubes:
            i = randint(0, len(self.__initCubes)-1)
            j = randint(0, len(self.__initCubes)-1)
            while matrix[i][j] != Cube(-1, -1):
                i = randint(0, len(self.__initCubes) - 1)
                j = randint(0, len(self.__initCubes) - 1)
            matrix[i][j] = c
        return matrix

    def __len__(self):
        return len(self.__initCubes)

    def printTest(self):
        m = self.getMatrix()
        for i in range(0, len(m)):
            for j in range(0, len(m)):
                if(m[i][j] != Cube(-1, -1)):
                    print("M[" + str(i) + "][" + str(j) + "]=" + str(m[i][j]) + " ")
        print("\n")