#!/usr/bin/python3
"""This module is about processing island perimeter
"""


def island_perimeter(grid):
    """return island perimeter
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
