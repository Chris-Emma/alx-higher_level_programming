#!/usr/bin/python3

"""
Same Module details as 10-student.py

A dictionary value will be the value of the public attribute
"""


class Student:
    """
    Class that defines a Student
    """
    def __init__(self, first_name, last_name, age):
        """ Initialize the class objects
        Args: first_name, last_name & age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieve dict representation of Student instance
        """
        if attrs is None:
            return self.__dict__
        if not isinstance(attrs, list):
            return self.__dict__
        if not (isinstance(attrs[elements], str) for elements in attrs):
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
