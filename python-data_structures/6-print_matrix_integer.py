#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j > 0 and j < len(matrix[i]):
                print(" ", end="")
            print("{:d}".format(matrix[i][j]), end="")
        print()
