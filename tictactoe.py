# Tic-Tac-Toe

import random
import time

def drawBoard(board):
	# draw the board with ascii
	# board is 2d matrix but player input is integer
	# for the player the board is:
	# [1,2,3]
	# [4,5,6]
	# [7,8,9]                            

	print(board[0][0] + '|' + board[1][0] + '|' + board[2][0])
	print('-+-+-')
	print(board[0][1] + '|' + board[1][1] + '|' + board[2][1])
	print('-+-+-')
	print(board[0][2] + '|' + board[1][2] + '|' + board[2][2])

def inputPlayerLetter():
	# player chooses which letter they want to be

	letter = ''
	while not (letter == 'X' or letter == 'O'):
		print('Do you want to be X or O?')
		letter = input().upper()

	# return [player's letter, computer's letter]
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def whoGoesFirst():
	# randomly choose who goes first
	
	if random.randint(1, 100) <= 50:
		return 'computer'
	else:
		return 'player'

def makeMove(board, letter, move):
	# this function changes the original list
	# look up list references if confused
	
	board[(move-1)%3][(move-1)//3] = letter

def isWinner(bo, le, move):
	# a winning move can only happen on the most recent move
	# search the row, column, diag of that most recent move

	row, col = ( (move-1)%3, (move-1)//3 )


def isSpaceFree(board, move):
	return board[(move-1)%3][(move-1)//3] == ' '

def getFreeSpaces(board):
	FreeSpace = []
	for space in range(1,10):
		if board[(move-1)%3][(move-1)//3] == ' ':
			FreeSpace.append(space)

	return FreeSpace

def getPlayerMove(board):
	# this function makes use of short circuiting in python
	# quick reminder: if you swapped the two statements in the while line, the function would error if we input 'Z'

	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		print('What is your next move? (1-9)')
		move = input()
	return int(move)

def getComputerMove(board):
	# TODO: make it take in an agent, board and freespaces

	# random agent
	availableMoves = getFreeSpaces(board)
	print('computer is thinking... ', availableMoves)
	return random.choice(availableMoves)

print('Welcome to Tic-Tac-Toe!')

playerletter, computerletter = inputPlayerLetter()
print()

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

turn = whoGoesFirst()
print(turn, 'goes first')
print()

drawBoard(board)
print()

# # simulate 2 rounds
# for i in range(0,4):
# 	if turn == 'player':
# 		playerMove = getPlayerMove(board)
# 		print()
# 		makeMove(board, playerletter, move=playerMove)
# 		drawBoard(board)
# 		print()

# 		turn = 'computer'
# 	else:
# 		computerMove = getComputerMove(board)
# 		time.sleep(2)
# 		print(computerMove)
# 		time.sleep(0.5)
# 		print()
# 		makeMove(board, computerletter, move=computerMove)
# 		# drawBoard(board)
# 		# print()

# 		turn = 'player'
