#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """function print matrix

    Args:
        matrix: matrix list

    Returns:
        None
    """
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end='')
        print()
