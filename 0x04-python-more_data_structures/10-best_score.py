#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        y = sorted((value, key)
                   for (key, value) in a_dictionary.items()).pop()[1]
        return (y)
