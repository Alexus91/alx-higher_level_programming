#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix."""
    new_matrix = matrix.copy()

    for idx in range(len(matrix)):
        new_matrix[idx] = list(map(lambda x: x**2, matrix[idx]))

    return (new_matrix)
