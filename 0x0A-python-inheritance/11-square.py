#!/usr/bin/python3


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        a = self.__size * self.__size
        return a

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
    
