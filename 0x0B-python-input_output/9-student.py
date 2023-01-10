#!/usr/bin/python3
"""
Module 9-student
Defines class Student
with public method
"""


class Student():
    """
    Functions:
      __init__(self, first_name, last_name, age)
      to_json(self)
    Args:
      first_name (str): public instance
      last_name (str): Public instance
      age (int): public instance
    """
    def __init__(self, first_name, last_name, age):
        """
        Initilizes Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        object to json
        """
        return self.__dict__
