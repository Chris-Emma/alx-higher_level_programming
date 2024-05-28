#!/usr/bin/python3

"""
Pascal Triangle Module.
"""


def pascal_triangle(n):
    """
    Function to generate the Pascal Triangle up to the nth row
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = []
    for i in range(n):
        row = [1]

        if i > 1:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                new_element = prev_row[j - 1] + prev_row[j]
                row.append(new_element)

        if i > 0:
            row.append(1)

        triangle.append(row)

    return triangle
