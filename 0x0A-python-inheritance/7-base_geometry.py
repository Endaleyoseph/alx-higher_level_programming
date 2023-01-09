#!/usr/bin/python3
"""
Modlue 7-base_geometry
Defines class BaseGeomtry
with public instance method,
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
