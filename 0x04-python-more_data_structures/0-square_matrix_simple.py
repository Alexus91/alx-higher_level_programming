#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nw_mtx = matrix.copy()
    for indx in range(len(matrix)):
        nw_mtx[indx] = list(map(lambda x: x**2, matrix[indx]))
        return (nw_mtx)
