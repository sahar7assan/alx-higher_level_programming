#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """function computes the square value of all integers of a matrix

    Args:
        matrix: matrix list

    Returns:
        square matrix
    """
    new_matrix = [[x**2 for x in row] for row in matrix]
    return new_matrix
