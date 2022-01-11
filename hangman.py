import random
from typing import ChainMap

name = input('What is your name?: ')
print(f'Goodluck {name}! ')

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
guesses = ''
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed += 1

    if failed == 0:
        print('You Win! ')
        print(f'The word is: {word}.')
        break

    guess = input('Guess the letter: ')
    guesses += guess

    if guess not in word:
        turns -= 1
        print('Guess again')
        print(f'You have {turns} turns left...')

    if turns == 0:
        print('You have lost...')
