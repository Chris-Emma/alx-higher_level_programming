#!/usr/bin/python3

""" Module to return the dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    Class to json object
    Return:
        The dict for JSON serialization of an object
    """
    return obj.__dict__
