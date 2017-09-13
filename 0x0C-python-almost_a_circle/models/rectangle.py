#!/usr/bin/python3
'''
Module for the Rectangle class
'''


from models.base import Base


class Rectangle(Base):
    '''
    initializes the Rectangle class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
        getter for Rectangle width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        setter for Rectangle width
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
        getter for Rectangle height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        setter for Rectangle height
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
        getter for Rectangle x
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        setter for Rectangle x
        '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
        getter for Rectangle y
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        setter for y
        '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        returns area of Rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''
        prints in stdout instance with character #
        '''
        print('\n' * self.__y, end='')
        for i in range(self.__height):
            print((' ' * self.__x) + (self.__width * '#'))

    def __str__(self):
        '''
        overloads the __str__ that returns Rectangle
        '''
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id,
                self.x,
                self.y,
                self.width,
                self.height))

    def to_dictionary(self):
        '''
        returns the dict representation of Rectangle
        '''
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['width'] = self.width
        my_dict['height'] = self.height
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        return my_dict

    def update(self, *args):
        '''
        assigns argument to each attribute
        '''
        for x, y in enumerate(args):
            if x == 0:
                self.id = y
            elif x == 1:
                self.width = y
            elif x == 2:
                self.height = y
            elif x == 3:
                self.x = y
            elif x == 4:
                self.y = y
