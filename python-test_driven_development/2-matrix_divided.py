#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """def name: matrix_divided"""
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    newmat = []
    for elements in matrix:
        text = "matrix must be a matrix (list of lists) of integers/floats"
        if type(elements) is not list:
            raise TypeError(text)
        new_list = []
        for i in elements:
            if type(i) is not int and type(i) is not float:
                raise TypeError(text)
            x = i / div
            new_list.append(round(x, 2))
        newmat.append(new_list)
    for r in matrix:
        if len(r) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    return newmat
