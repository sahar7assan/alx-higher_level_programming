#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """function print matrix

    Args:
        matrix: matrix list

    Returns:
        None
    """
    if matrix None:
        return
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end='')
        print()
