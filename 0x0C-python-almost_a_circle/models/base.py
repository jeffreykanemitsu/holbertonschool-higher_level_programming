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
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes the json string representation of list_objs to a file
        '''
        js = []
        for obj in list_objs:
            js.append(obj.to_dictionary())
        js = Base.to_json_string(js)
        with open("{:s}.json".format(cls.__name__), 'w') as fn:
            fn.write(js)

    @staticmethod
    def from_json_string(json_string):
        '''
        returns list of json_string representation
        '''
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        returns an instance with all attributes already set
        '''
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
