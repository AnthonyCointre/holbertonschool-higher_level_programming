#!/usr/bin/python3
"""def matrix_divided"""


def matrix_divided(matrix, div):
	"""divides all elements of a matrix"""

	if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	if not all(isinstance(ele, (int, float)) for row in matrix for ele in row):
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	row_length = len(matrix[0])
	if any(len(row) != row_length for row in matrix):
		raise TypeError("Each row of the matrix must have the same size")
	if not isinstance(div, (int, float)):
		raise TypeError("div must be a number")
	if div == 0:
		raise ZeroDivisionError("division by zero")
	return [[round(ele / div, 2) for ele in row] for row in matrix]
