#!/usr/bin/python3
"""
Module 103-magic_class
Defines class MagicClass
"""
import math


class MagicClass:
    """
    definition of magic class
    Attributes:
           radius : radius of a circle
    """
    def __init__(self, radius=0):
        """
        Initilizes magic class
        Args:
          radius : radius of a circle
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        computes the area of a circle
        Return: the area of the circle
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        computes the circumference of a circle
        Return: the circumference of a circle
        """
        return 2 * math.pi * self.__radius
