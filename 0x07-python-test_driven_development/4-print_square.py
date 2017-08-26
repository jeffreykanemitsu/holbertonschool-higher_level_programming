#!/usr/bin/python3
"""
Prints a square with the character '#'
"""


def print_square(size):
    typeerr = 'size must be an integer'
    if not isinstance(size, int):
        raise TypeError(typeerr)
    if size < 0:
        raise ValueError('size must be >= 0')
    if not isinstance(size, float) and size < 0:
        raise TypeError(typeerr)

    for x in range(size):
        print('#' * size)
