#!/usr/bin/python3
'''N-Queens Problem'''
import sys
from typing import List

def exit_seq(msg: str):
	'''Prints message and exits with status 1'''
	print(msg)
	sys.exit(1)

def place_queen(board, row):
	if row >= len(board):
		return
	for col in range(len(board)):
		if is_safe(board, row, col):
			board[row][col] = 1
			place_queen(board, row + 1)
		else:
			board[row][col] = 3
	


def is_safe(board, row, col):
	'''Checks if a position is safe'''
	if row >= 0 and col >= 0:
		for i in range(len(board)):
			if board[row][i] == 1:
				return False
			
		# if not all(board[row]):
		# 	return False
	return True


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
	board = [[0 for i in range(n_queens)]
		  	 for i in range(n_queens)]
	[print(board[i]) for i in range(n_queens)]

	print("---------")

	board[2][2] = 2
	board[0][1] = 5

	place_queen(board, 0)

	[print(board[i]) for i in range(n_queens)]

	print("---------")

	place_queen(board, 0)

	[print(board[i]) for i in range(n_queens)]