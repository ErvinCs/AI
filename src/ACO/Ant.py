from copy import deepcopy

class Ant:
    def __init__(self, cubes):
        '''
        :param cubes: list of Cube; form the solution
        '''
        self.__cubes = deepcopy(cubes)
        self.__path = []
        self.__index = -1
        self.__fitness = 0

    def getPath(self):
        return self.__path

    def getFitness(self):
        self.fitness()
        return self.__fitness

    def getCubes(self):
        return self.__cubes

    def getCube(self, index):
        return self.__path[index]

    def getTopCube(self):
        return self.__path[len(self.__path)-1]

    def incrementIndex(self):
        self.__index += 1

    #Update
    def addCube(self, cube):
        '''
        Add a Cube to __path (update)
        Removes the Cube from the list of (possible) Cubes
        :param cube: Cube
        :raise: Exception - won't happen again
        '''
        if cube not in self.__cubes:
            raise Exception("Visited Cube!")

        self.incrementIndex()
        self.__path.append(cube)
        self.__cubes.remove(cube)
        return cube

    #Evaluate
    def fitness(self):
        '''
        Higher with the number of incorrect cubes (evaluate)
        :return: integer - self fitness
        '''
        self.__fitness = 0
        for i in range(1, len(self.__path)):
            if self.__path[i - 1].getSize() > self.__path[i].getSize():
                self.__fitness += 1
            if self.__path[i - 1].getColor() == self.__path[i].getColor():
                self.__fitness += 1
        return self.__fitness

    def __contains__(self, item):
        return (item in self.__path)

    def __eq__(self, other):
        return (self.getPath() == other.getPath())

    def __ne__(self, other):
        return (self.getPath() != other.getPath())

    def __str__(self):
        string = ""
        for cube in self.__path:
            string += str(cube) + "\n"
        return string
