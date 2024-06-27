#!/usr/bin/python3
'''Island perimeter module'''

def island_perimeter(grid):
	'''Island perimeter function'''
	if not grid or len(grid) < 1:
		return 0
	length = len(grid[0])
	island_breadth = 0
	island_length = 0

	for i in range(length - 1):
		breadth_counter = 0
		length_counter = 0
		for j in range(length - 1):
			length_counter = length_counter + 1 if grid[i][j] else length_counter
		for j in range(length - 1):
			breadth_counter = breadth_counter + 1 if grid[j][i] else breadth_counter
		island_breadth = breadth_counter if breadth_counter > island_breadth else island_breadth
		island_length = length_counter if length_counter > island_length else island_length
	
	perimeter = 2 * (island_length + island_breadth)
	return perimeter
