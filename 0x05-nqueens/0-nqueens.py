#!/usr/bin/python3
'''N-Queens Problem'''
import sys
from typing import List

def exit_seq(msg: str):
	'''Prints message and exits with status 1'''
	print(msg)
	sys.exit(1)

def is_safe(pos: List[int], solution: List[List[int]]):
	'''Checks if a position is safe'''
	

if __name__ == '__main__':
	args = sys.argv
	n_queens = 0
	if len(args) != 2:
		exit_seq("Usage: nqueens N")
	try:
		n_queens = int(args[1])
	except (TypeError, ValueError):
		exit_seq("N must be a number")
	if n_queens < 4:
		exit_seq("N must be at least 4")