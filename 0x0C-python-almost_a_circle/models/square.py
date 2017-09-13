#!/usr/bin/python3
'''
Module for the Square class
'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    initializes the Square class
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        '''
        getter for square size
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        setter for square size
        '''
        self.width = value
        self.height = value

    def __str__(self):
        '''
        overloads the __str__ that rturns square
        '''
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id,
            self.x,
            self.y,
            self.size)

    def to_dictionary(self):
        '''
        returns the dict representation of Rectangle
        '''
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['size'] = self.size
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        return my_dict

    def update(self, *args, **kwargs):
        '''
        assigns attributes in the class Square
        '''
        for x, val in enumerate(args):
            if x == 0:
                self.id = val
            if x == 1:
                self.size = val
            if x == 2:
                self.x = val
            if x == 3:
                self.y = val

        for key, val in kwargs.items():
            if key == 'id':
                self.id = val
            elif key == 'size':
                self.size = val
            elif key == 'x':
                self.x = val
            elif key == 'y':
                self.y = val
