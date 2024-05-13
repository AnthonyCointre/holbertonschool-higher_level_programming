#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            end_char = " " if i < len(row) - 1 else ""
            print("{:d}{}".format(num, end_char), end="")
        print()
