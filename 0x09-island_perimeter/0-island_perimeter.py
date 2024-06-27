#!/usr/bin/python3
'''Island perimeter module'''

def island_perimeter(grid):
	'''Island perimeter function'''
	length = len(grid[0])
	breadth = 0

	for i in range(length - 1):
		counter = 0
		for j in range(length - 1):
			counter = counter + 1 if grid[j][i] else 0
		breadth = counter if counter > breadth else breadth
	
	perimeter = 2 * (length + breadth)
	return perimeter
