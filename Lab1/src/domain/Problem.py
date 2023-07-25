from src.domain.State import State
from copy import deepcopy
from math import sqrt


class Problem:
    def __init__(self, filename):
        '''
        :param filename: path of a file - contains the board size and the initial board state
        initState - initial board state read from file
        '''
        self.__fileName = filename
        self.__state = self.readFile()
        self.__initState = deepcopy(self.__state)

    def getState(self):
        return self.__state

    def getInitState(self):
        return self.__initState

    def setState(self, newState):
        self.__state = newState

    def findSpot(self):
        '''
        :return: (row, col) - coordinates of an empty spot on the board
        '''
        for row in range(0, self.__state.getSize()):
            for col in range(0, self.__state.getSize()):
                if self.__state.getBoard()[row][col] == 0:
                        return (row, col)
        return (-1, -1)

    def expand(self, state):
        '''
        :param state: to expand
        :return: list of State
            Each state from the list has the next empty spot filled with each valid value
        '''
        stateList = []
        row, col = self.findSpot()
        if (row, col) == (-1, -1):
            return False

        for key, val in state.getNumbers().items():
            ok = True
            item = key
            for i in range(row + 1, self.__state.getSize()):
                if item == self.__state.getBoard()[i][col]:
                    ok = False
                    break
            if ok is True:
                for i in range(0, row):
                    if item == self.__state.getBoard()[i][col]:
                        ok = False
                        break
            if ok is True:
                for i in range(col + 1, self.__state.getSize()):
                    if item == self.__state.getBoard()[row][i]:
                        ok = False
                        break
            if ok is True:
                for i in range(0, col):
                    if item == self.__state.getBoard()[row][i]:
                        ok = False
                        break
            if ok is True:
                root = int(sqrt(self.__state.getSize()))
                qrow = int(row/root) * root
                qcol = int(col/root) * root
                for i in range(qrow, qrow+root):
                    for j in range(qcol, qcol+root):
                        if item == self.__state.getBoard()[i][j]:
                            ok = False
                            break

            if ok is True:
                state.setItem(row, col, key)
                stateList.append(deepcopy(state))
                state.decrNumber(key)
        return stateList

    def heuristics(self, state1, state2, row, col):
        '''
        :param state1: State + a value
        :param state2: State + a different value
        :param (row, col): coordinates of the last filled spot
        :return: the state with more equal values
        '''
        item1 = state1.getBoard()[row][col]
        item2 = state2.getBoard()[row][col]
        n1 = state1.getNumbers()
        n2 = state2.getNumbers()
        if n1[item1] < n2[item2]:
            return state1
        return state2



    def readFile(self):
        '''
        Reads the board from a text file
        '''
        f = open(self.__fileName, "r")
        size = int(f.readline())
        values = []
        numbers = {i: size for i in range(1, size + 1)}
        lines = f.readlines()
        for line in lines:
            line.strip()
            line = line.split()
            i = 0
            while i < len(line):
                line[i] = int(line[i])
                if line[i] != 0:
                  numbers[line[i]] -= 1
                i += 1
            values.append(line)
        f.close()
        state = State(size, values)
        state.setNumbers(numbers)
        return state