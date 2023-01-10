#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of ints"""
    for row in matrix:
        for i in row:
            if i != row[-1]:
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end="")
        print()
