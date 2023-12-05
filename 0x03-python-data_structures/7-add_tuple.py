#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    length_A = len(tuple_a)
    length_B = len(tuple_b)

    if length_A < 1:
        tuple_a = (0, 0)
    elif length_A < 2:
        tuple_a = (tuple_a[0], 0)

    if length_B < 1:
        tuple_b = (0, 0)
    elif lenB < 2:
        tuple_b = (tuple_b[0], 0)

    res = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return res
