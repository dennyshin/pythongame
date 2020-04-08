# tic-tac-toe

import random
import time

# returns [playerletter, computerletter]
def getPlayerLetter():
	letter = ''
	while not (letter == 'X' or letter == 'O'):
		letter = input('Do you want to be X or O? ').upper()
	
	if letter == 'X':
		return ['X','O']
	else:
		return ['O','X']

# board[0] is ignored
def drawBoard(b):
	print(b[1]+'|'+b[2]+'|'+b[3])
	print('-+-+-')
	print(b[4]+'|'+b[5]+'|'+b[6])
	print('-+-+-')
	print(b[7]+'|'+b[8]+'|'+b[9])

# choose who goes first
def whoGoesFirst():
	if random.randint(0,1) == 0:
		return ['computer', 'player']
	else:
		return ['player', 'computer']

# find open spots on board
def getValidMoves(b):
	return [i for i,e in enumerate(b) if e == ' '][1:]

def getPlayerMove(validmoves):
	move = ''
	while move not in validmoves:
		move = int(input('Your move (1-9): '))

	return move

# currently random move AI
# TODO: extend this to import an AI
def getComputerMove(validmoves):
	return random.choice(validmoves)

# brute force. not scalable
def checkWin(b, turn):
	# draw
	# TODO: draws can be seen earlier
	if getValidMoves(b) == []:
		return 'DRAW'



# start game
print('TIC-TAC-TOE\n')

playerletter, computerletter = getPlayerLetter()
player1, player2 = whoGoesFirst()
turn = player1

board = [' ']*10
drawBoard(board)

# turns
# start loop here
for i in range(3):
	print(turn + "'s turn.")
	if turn == 'player':
		playermove = getPlayerMove(getValidMoves(board))
		board[playermove] = playerletter
		turn = 'computer'
	else:
		print('computer is thinking...')
		time.sleep(2)
		computermove = getComputerMove(getValidMoves(board))
		board[computermove] = computerletter
		turn = 'player'

	drawBoard(board)