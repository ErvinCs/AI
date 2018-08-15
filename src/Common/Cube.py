from random import randint

class Cube:
    def __init__(self, size, color):
        '''
        :param size: integer
        :param color: integer
        '''
        self.__size = size
        self.__color = color

    def getSize(self):
        return self.__size

    def getColor(self):
        return self.__color

    def setSize(self, size):
        self.__size = size

    def setColor(self, color):
        self.__color = color

    def __str__(self):
        '''
        :return: string representation of the Cube
            color * size
        '''
        string = ""
        for i in range(0, self.__size):
            string += str(self.__color)
        return string

    def __eq__(self, other):
        '''
        :param other: Cube
        :return: True if self is equal with other; False otherwise
            Two cubes are equal if they have the same size and the same color
        '''
        return (self.getSize() == other.getSize() and self.getColor() == other.getColor())

    def __ne__(self, other):
        '''
        :param other: Cube
        :return: True if self is not equal with other; False otherwise
            Two cubes are equal if they have the same size and the same color
        '''
        return (self.getSize() != other.getSize() or self.getColor() != other.getColor())