#!/usr/bin/python3

"""
Search and Update Module.
You are not allowed to import any module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text into a file after each line
    containing a specific string.
    """
    with open(filename, 'r', encoding="UTF8") as my_file:
        lines = my_file.readlines()

    with open(filename, 'w', encoding="UTF8") as my_file:
        for line in lines:
            my_file.write(line)
            if search_string in line:
                my_file.write(new_string)
