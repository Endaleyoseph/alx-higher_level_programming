#!/usr/bin/python3
"""
Module 12-pascal_triangle
Defines pascal_trinagle
makes nxn pascal triangle
"""


def pascal_triangle(n):
    """
    Returns list of list of integers
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for row in range(n - 1):
        lst = [1]
        for i in range(row):
            lst.append(triangle[-1][i] + triangle[-1][i + 1])
        lst.append(1)
        triangle.append(lst)

    return triangle
