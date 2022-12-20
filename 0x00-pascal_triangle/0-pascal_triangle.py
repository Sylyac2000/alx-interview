#!/usr/bin/python3
"""
function to generate pascal triangle of a given number
"""


def pascal_triangle(n):
    """
    Prints out a Pascal triangle with `n` number of rows.
    """
    if n < 0:
        return []
    triangle = []
    for i in range(n):
        ligne = []
        ligne.append(1)
        for j in range(1, i):
            ligne.append(triangle[i-1][j-1] + triangle[i-1][j])
        if i != 0:
            ligne.append(1)
        triangle.append(ligne)

    return triangle
