#!/usr/bin/python3
"""
Module 11-sqaure
Defines class square
with initilization
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Inherites from class rectangle
    Functions:
      __init__
    """
    def __init__(self, size):
        """
        Initilizes square
        Args:
           size (int): private instance
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        returns the area of sqaure
        """
        return self.__size * self.__size

    def __str__(self):
        """
        prints a square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
