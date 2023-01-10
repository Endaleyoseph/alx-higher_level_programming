#!/usr/bin/python3
"""
Module 10-student
Defines class Student
with public method
"""


class Student():
    """
    Functions:
      __init__(self, first_name, last_name, age)
      to_json(self, attrs)
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

    def to_json(self, attrs=None):
        """
        object to json
        """
        if attrs is not None:
            dic = {}
            for i in attrs:
                if i in self.__dict__.keys():
                    dic[i] = self.__dict__[i]
            return dic
        else:
            return self.__dict__
