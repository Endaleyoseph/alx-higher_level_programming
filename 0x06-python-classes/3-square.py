#!/usr/bin/python3
"""
Module 2-square
Defines a class Square with private instance atribute,
and public instance method
"""


class Square:
    """
    Definition of class square with private instance,
    and public method

    Args:
        size : size of the square
    """
    def __init__(self, size=0):
        """
        Initilizes a square with size that has a defualt value of 0

        Attributes:
            size(int) : size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        This method calculates area of the square

        Returns:
           area(int) : the current square area
        """
        return self.__size ** 2
