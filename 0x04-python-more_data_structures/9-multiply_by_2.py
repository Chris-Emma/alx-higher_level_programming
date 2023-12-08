#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDic = {}
    if a_dictionary:
        for j in a_dictionary:
            newDic[j] = a_dictionary[j] * 2
    return (newDic)
