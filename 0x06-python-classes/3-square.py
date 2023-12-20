#!/usr/bin/python3


""" defines a square """


class Square:
    """ square with private instance attribute size """

    def __init__(self, size=0):
        """ Initializes square """
        if type(size) == int:
            if size >= 0:
                self._size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Finds and returns area of square """
        return (self._size * self._size)
