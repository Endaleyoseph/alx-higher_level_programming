#!/usr/bin/python3
"""
Module 4-print_square
Defines print_square
prints a square based on given size
"""


def print_square(size):
    """
    prints a square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("", end="")
    else:
        for i in range(size):
            print("#" * size)
