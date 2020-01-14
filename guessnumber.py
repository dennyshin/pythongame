# Guess the Number Game

import random

# generate random number
number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# allow max 6 guesses
for guessesTaken in range(1,7):
	guess = int(input('Take a guess: '))

	if guess < number:
		if guessesTaken != 6:
			print('Your guess is too low.')
			if guessesTaken == 5:
				print('You have 1 guess left.')
			else:
				print('You have ' + str(6-guessesTaken) + ' guesses left.')
			print()
	
	elif guess > number:
		if guessesTaken != 6:
			print('Your guess is too high.')
			if guessesTaken == 5:
				print('You have 1 guess left.')
			else:
				print('You have ' + str(6-guessesTaken) + ' guesses left.')
			print()

	elif guess == number:
		break

if guess == number:
	print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
	print('No! The number I was thinking of was ' + str(number) + '.')
