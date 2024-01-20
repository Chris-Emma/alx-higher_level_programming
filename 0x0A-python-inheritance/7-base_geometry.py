#!/usr/bin/python3
"""
    class BaseGeometry based on '6-base_geometry.py'
"""


class BaseGeometry:
    """ empty class """

    def area(self):
        """ raises an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value is an int """
        if type(value) is not int:
            raise TypeError("{}  must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
