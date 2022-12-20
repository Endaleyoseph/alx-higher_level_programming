#!/usr/bin/python3
"""
Module 5-square
Defines a class Square with private instance atribute,
public instance method, can access and update size, and
can also print square with #
"""


class Square:
    """
    Definition of class square with private instance,
    and public

    Args:
        size : size of the
    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
        my_print(self)
    """
    def __init__(self, size=0):
        """
        Initilizes a square with size that has a defualt value of 0

        Attributes:
            size(int) : size of the
        """
        self.__size = size

    @property
    def size(self):
        """
        This function is used to retrieve

        Returns:
             size(int) : size of the
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This function is used to set a

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
        This method calculates area of the

        Returns:
           area(int) : the current square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #
        if size is 0 prints empty
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
