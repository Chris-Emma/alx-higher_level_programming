#!/usr/bin/python3

if __name__ == "__main__":
    """Prints results of add of all args"""
from sys import argv
add = 0
for i in argv[1:]:
    add = add + int(i)
print("{:d}".format(add))
