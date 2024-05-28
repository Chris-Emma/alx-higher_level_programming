#!/usr/bin/python3

"""
Student class Module
You are not allowed to import any module
"""


class Student:
    """
    Class that defines a Student
    """
    def __init__(self, first_name, last_name, age):
        """ Initialize the class objects
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieve dictionary representation of student
        """
        return self.__dict__
