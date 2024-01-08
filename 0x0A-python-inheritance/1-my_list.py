#!/usr/bin/python3
""" class MyList that inherits from list """

class MyList(list):
    """MyList inherits from a  list"""

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
