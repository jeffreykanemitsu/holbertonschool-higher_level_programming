#!/usr/bin/python3


def __init__(self, size):


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
    
