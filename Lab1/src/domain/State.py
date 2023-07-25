from math import sqrt

class State:
    def __init__(self, size, board):
        '''
        :param size: integer - sudoku board: sizeXsize
        :param board: 2d array
        numbers: dict - the values not yet placed on the board
        '''
        self.__size = int(size)
        self.__board = board
        self.__numbers = {i: size for i in range(1, size + 1)}

    def getNumbers(self):
        return self.__numbers

    def getSize(self):
        return self.__size

    def getBoard(self):
        return self.__board

    def getItem(self, x, y):
        return self.__board[x][y]

    def setNumbers(self, numbers):
        self.__numbers = numbers

    def setItem(self, x, y, val):
        self.__board[x][y] = val
        return self

    def decrNumber(self, number):
        self.__numbers[number] -= 1

    def isExhausted(self):
        '''
        :return: True if numbers is empty; False otherwise
        '''
        for key, value in self.__numbers.items():
            if self.__numbers[key] == 0:
                return False
        return True

    def isSolution(self):
        '''
        :return: True if the board is a solution i.e.
            No equal numbers on the same line
            No equal numbers on the same column
            No equal numbers in the same quadrant
        '''
        if not self.isExhausted():
            return False
        bound = sum(range(1, self.getSize() + 1))

        for i in range(0, self.getSize()):
            sumx = 0
            for j in range(0, self.getSize()):
                sumx += self.__board[i][j]
            if sumx != bound:
                return False

        root = int(sqrt(self.__size))
        for i in range(0, self.__size, root):
            for j in range(0, self.__size, root):
                sumx = 0
                for row in range(0, root):
                    for col in range(0, root):
                        sumx += self.__board[row + j][col + i]
                if (sumx != bound):
                    return False
        return True

    def __str__(self):
        '''
        :return: string representation of the board
        '''
        string = "\n----------\n"
        for line in self.__board:
            string += str(line) + "\n"
        string += "----------"
        return string

