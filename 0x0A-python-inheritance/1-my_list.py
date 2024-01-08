#!/usr/bin/python3
"""
contains the MyList class
"""

class MyList(list):
    """MyList inherits from a  list"""

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
