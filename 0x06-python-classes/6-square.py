#!/usr/bin/python3
class Square:
    """
    Defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

        if not (type(position[0]) == int) and type(position[1] == int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            for i in range(self.position[1]):
                print("")
            for x in range(self.__size):
                for y in range(self.__position[0]):
                    print(" ", end="")
                for z in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def position(self):
        return self.__position

    tupleerr = "position must be a tuple of 2 positive integers"

    @position.setter
    def position(self, value):
            if not (type(value[0] == int) and tpye(value[1] == int)):
                raise TypeError(tupleerr)
            elif value[0] < 0 or value[1] < 0:
                raise TypeError(tupleerr)
            else:
                self.__position = value
