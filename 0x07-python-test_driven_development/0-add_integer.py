#!/usr/bin/python3
"""
Returns the sum of two integers but raises a TypeError if the argument
is not an int or a float.
"""


def add_integer(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
