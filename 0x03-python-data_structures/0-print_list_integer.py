#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print all integers of a list using str.format()."""
    for number in my_list:
        print("{:d}".format(number))
