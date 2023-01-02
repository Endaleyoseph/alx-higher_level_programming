#!/usr/bin/python3
"""
Module 7-rectangle
Defines class Rectangle
with private attribute property and setter
and also public class attribute
Area and perimeter included
"""


class Rectangle:
    """
    contains private instance width and height,
    and public class attribute number_of_instances
    and print_symbol
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initilizes width and height
        Args:
          width : width of the rectangle
          height : height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        return the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width
        Arg:
         value: the size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height
        Arg:
          value: the size
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """
        Returns the area of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.height) + (2 * self.width)

    def __str__(self):
        """
        return string form of object using #
        """
        _str = ""
        if self.width == 0 or self.height == 0:
            return _str
        for i in range(self.__height):
            _str += str(self.print_symbol) * self.__width
            if i != self.height - 1:
                _str += "\n"
        return _str

    def __repr__(self):
        """
        return the representation of the string
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        prints a message when an instance is deleted
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
