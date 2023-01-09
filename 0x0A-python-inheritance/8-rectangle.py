#!/usr/bin/python3
"""
Modlue 8-rectangle
Defines class BaseGeomtry
with public instance method
Defines class Rectangle
Inherites from BaseGeometry
"""


class BaseGeometry:
    """
    Functions:
     area
     integer_validator
    """
    def area(self):
        """
        computes the area of the geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        Args:
         name(str): name
         value(int): the value to be validated
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry
    Functions:
     __init__
    """
    def __init__(self, width, height):
        """
        Initilizes Rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
