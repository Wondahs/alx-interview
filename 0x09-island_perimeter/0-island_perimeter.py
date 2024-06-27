#!/usr/bin/python3
'''Island perimeter module'''


def island_perimeter(grid):
    '''Island perimeter function'''
    if not grid:
        return 0
    length = len(grid[0])
    i_breadth = 0
    i_length = 0

    for i in range(length - 1):
        length_counter = 0
        for j in range(length - 1):
            length_counter = length_counter + 1 \
                if grid[i][j] else length_counter
        for j in range(length - 1):
            if grid[i][j]:
                i_breadth += 1
                break
        i_length = length_counter \
            if length_counter > i_length else i_length

    perimeter = 2 * (i_length + i_breadth)
    return perimeter
