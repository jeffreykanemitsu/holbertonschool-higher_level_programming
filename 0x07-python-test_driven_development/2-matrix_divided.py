#!/usr/bin/python3
"""
Returns a new matrix with all elements divided.
"""


def matrix_divided(matrix, div):
    typeerr = 'matrix must be a matrix (list of lists) of integers/floats'
    sizeerr = 'Each row of the matrix must have the same size'
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(typeerr)
        if len(row) != len(matrix[0]):
            raise TypeError(sizeerr)

    for row in matrix:
        for x in range(len(row)):
            if not isinstance(row[x], (int, float)):
                raise TypeError(typeerr)

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
