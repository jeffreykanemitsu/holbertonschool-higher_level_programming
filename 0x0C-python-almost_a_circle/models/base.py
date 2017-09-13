#!/usr/bin/python3
'''
Module for the Base class
'''
import json


class Base:
    '''
    Base class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        initializes the Base object
        '''
        if id is not None:
            '''
            assigns the public instance attribute id to this argument value
            '''
            self.id = id
        else:
            '''
            increment object & assign value to the public instance attribute id
            '''
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        returns json string representation
        '''
        if list_dictionaries is None:
            return {}
        else:
            return json.dumps(list_dictionaries)
