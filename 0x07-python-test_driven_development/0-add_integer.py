#!/usr/bin/python3

"""
This module is called '0_add_integer'
It supplies add_integer(a,b)
"""

def add_integer(a, b=98):
    """Returns rsult of addition of a,b"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
