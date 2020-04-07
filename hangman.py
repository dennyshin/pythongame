# HANGMAN

import random

HANGMAN_STATES = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 O   |
     |
     |
    ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\\  |
     |
    ===''', '''
 +---+
 O   |
/|\\  |
/    |
    ===''', '''
 +---+
 O   |
/|\\  |
/ \\  |
    ===''']

wordlist = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

# get random word
def getRandomWord(wordlist):
	return random.choice(wordlist)

# display board
def displayBoard(secret_word, HANGMAN_STATES, correct, wrong):
	display_word = list("_ "*len(secret_word))
	for letter in correct:
		idx = [i for i, e in enumerate(secret_word) if e == letter]
		for i in idx:
			display_word[i*2] = letter
	print("".join(display_word))

	print(HANGMAN_STATES[len(wrong)])
	print()

	# display wrong guesses
	for letter in wrong:
		print(letter, end=' ')
	print()

# get player guess
# could use getch package
def getGuess(already_guessed):
	while True:
		guess = input('guess a letter: ')

		if len(guess) != 1:
			print('enter a single letter')
		elif guess in already_guessed:
			print('you already guessed that letter')
		elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
			print('enter a letter')
		else:
			return guess.lower()

# start game
print('H A N G M A N\n')
secret_word = getRandomWord(wordlist)
print(secret_word)
correct = []
wrong = []
displayBoard(secret_word, HANGMAN_STATES, correct, wrong)

while True:
	guess = getGuess(correct+wrong)
	if guess in secret_word:
		correct.append(guess)
	else:
		wrong.append(guess)

	displayBoard(secret_word, HANGMAN_STATES, correct, wrong)

	# check win or lose
	if len(wrong) == 6:
		print('YOU LOSE!')
		print('The word was "{}"'.format(secret_word))
		break

	if set(secret_word) == set(correct):
		print('YOU WIN!')
		break