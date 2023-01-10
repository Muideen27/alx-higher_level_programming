#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """Print matrix containing int"""
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
                print("{:d}".format(matrix[x][y]), end="")
                if y != (len(matrix[x]) - 1):
                    print(" ", end="")

        print("")
