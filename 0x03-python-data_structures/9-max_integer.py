#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    bigger = my_list[0]
    for i in range(1, len(my_list)):
        if bigger < my_list[i]:
            bigger = my_list[i]
        else:
            continue
    return bigger
