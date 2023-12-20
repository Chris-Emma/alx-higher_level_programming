#!/usr/bin/python3


""" defines class square """


class Square:
    """ Represents square """

    def __init__(self, size=0):
        """ Initializes sqaure """
        self.size = size

    def area(self):
        """Calculates area of square"""
        return (self._size * self._size)

    @property
    def size(self):
        """Gets __self, returns size of sqaure"""
        return self._size

    @size.setter
    def size(self, value):
        """Sets size of square"""
        if type(value) == int:
            if value >= 0:
                self._size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
