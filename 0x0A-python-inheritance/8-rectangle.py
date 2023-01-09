#!/usr/bin/python3
"""
Modlue 8-rectangle
Defines class Rectangle
Inherites from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry
    Functions:
     __init__
    """
    def __init__(self, width, height):
        """
        Initilizes Rectangle
        Args:
          width (int): private
          height (int): private
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
