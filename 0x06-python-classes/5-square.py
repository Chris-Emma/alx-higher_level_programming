#!/usr/bin/python3


"""defines class square """


class Square:
    """The summary line for a class docstring should fit on one line."""

    def __init__(self, size=0):
        """The summary line for a class docstring should fit on one line."""
        self.size = size

    def area(self):
        """The summary line for a class docstring should fit on one line."""
        return (self._size * self._size)

    @property
    def size(self):
        """The summary line for a class docstring should fit on one line."""
        return self._size

    @size.setter
    def size(self, value):
        """The summary line for a class docstring should fit on one line."""
        if type(value) == int:
            if value >= 0:
                self._size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """The summary line for a class docstring should fit on one line."""
        i, j = 0, 0
        if self._size == 0:
            print()
        else:
            while i < self._size:
                while j < self._size:
                    print("#", end="")
                    j += 1
                print()
                j = 0
                i += 1
