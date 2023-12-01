#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order using str.format()."""
    for n in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[n]))
