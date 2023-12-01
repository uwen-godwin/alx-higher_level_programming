#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers using str.format()."""
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print()
