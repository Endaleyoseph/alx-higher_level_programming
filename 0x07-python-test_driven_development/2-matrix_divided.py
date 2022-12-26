#!/usr/bin/python3
"""
Module 2-matrix_divided
Definition of matrix_divided
divids a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Returns divided new matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    length = len(matrix[0])
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg)
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for j in row:
            if not isinstance(j, (int, float)):
                raise TypeError(msg)
    return list(map(lambda x: (list(map(lambda y:
                                        round(y / div, 2), x))), matrix))
