#!/bun/usr/python3
"""A module that multiply a 2D array with a given input"""


def matrix_divided(matrix, div):
    """
    Divides an arry element by div

    Args:
        matrix: @d array
        div: divisor

    Return: New array of divided element
    """

    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number") 

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")

    for i in range(len(matrix)):
        tmp_list = []
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            "of integers/floats")
        length = len(matrix[0])
        if len(matrix[i]) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(length):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")
            tmp_list.append(round(matrix[i][j]/div, 2))
        new_matrix.append(tmp_list)
    return new_matrix
