#!/usr/bin/python3
"""
    Contains class BaseGeometry and subclass Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Representation of the triangle """
    def __init__(self, width, height):
        """ An instantiation of the triangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
