#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 3]
]

matrix1 = [[]]
print(matrix_divided(matrix1, 3))
print(matrix_divided(matrix, 2))
print(matrix)
