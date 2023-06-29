#!/usr/bin/python3
"""
module that returns a list of integers
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1] + [
                prev_row[j] + prev_row[j + 1] for j in range(i - 1)
        ] + [1]
        triangle.append(new_row)

    return triangle
