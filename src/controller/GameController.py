from src.domain.Problem import Problem

class GameControler:
    def __init__(self, filename):
        '''
        :param filename: path of a file - contains the board size and the initial board state
        '''
        self.__problem = Problem(filename)

    def getProblem(self):
        return self.__problem

    def setProblem(self, newProblem):
        self.__problem = newProblem

    def BFS(self):
        '''
        Fills the board in a BFS manner
        :return: filled board
        '''
        toVisit = [self.__problem.getInitState()]
        while (len(toVisit) > 0):
            currState = toVisit.pop(0)
            self.__problem.setState(currState)
            if currState.isSolution():
                return currState

            stateList = self.__problem.expand(currState)
            if stateList is not False:
                for state in stateList:
                    toVisit.append(state)

    def GBFS(self):
        '''
        Fills the board in a GBFS manner
        :return: filled board
        '''
        toVisit = [self.__problem.getInitState()]
        while (len(toVisit) > 0):
            currState = toVisit.pop(0)
            self.__problem.setState(currState)
            if currState.isSolution():
                return currState

            row, col = self.__problem.findSpot()
            stateList = self.__problem.expand(currState)
            if stateList is not False and len(stateList) != 0:
                for state in stateList:
                    toVisit.append(state)

                best = stateList[0]
                for s in range(1, len(stateList)):
                    best = self.__problem.heuristics(best, stateList[s], row, col)
                toVisit.remove(best)
                toVisit.insert(0, best)


