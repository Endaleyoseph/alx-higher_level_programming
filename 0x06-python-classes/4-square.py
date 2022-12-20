#!/usr/bin/python3
"""
Module 4-square
Defines a class Square with private instance atribute,
public instance method, and can access and update size
"""


class Square:
    """
    Definition of class square with private instance,
    and public method

    Args:
        size : size of the square
    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
    """
    def __init__(self, size=0):
        """
        Initilizes a square with size that has a defualt value of 0

        Attributes:
            size(int) : size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        This function is used to retrieve size

        Returns:
             size(int) : size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This function is used to set a property

        Args:
            Value(int): size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This method calculates area of the square

        Returns:
           area(int) : the current square area
        """
        return self.__size ** 2
