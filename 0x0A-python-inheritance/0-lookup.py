#!/usr/bin/python3
"""
Contains the lookup function
"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return [method for method in dir(obj)]
