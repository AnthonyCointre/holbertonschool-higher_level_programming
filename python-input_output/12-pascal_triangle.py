#!/usr/bin/python3
"""
Returns a list of lists of integers representing
the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.
    """

    list = []

    if n <= 0:
        return list
    else:
        list.append([1])

    for i in range(1, n):

        row = [1]

        for j in range(1, i):
            row.append(list[i-1][j-1] + list[i-1][j])

        row.append(1)

        list.append(row)

    return list
