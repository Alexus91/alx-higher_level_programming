#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ computes the square value of all integers of a matrix."""
    nw_mtx = matrix.copy()

    for indx in range(len(matrix)):
        nw_mtx[indx] = list(map(lambda x: x**2, matrix[indx]))2
        return (nw_mtx)
