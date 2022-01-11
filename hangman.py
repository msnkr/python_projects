import random

name = input('What is your name?: ')
print(f'Goodluck {name}! ')

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
turns = 12

guesses = ''
while turns > 0:
    fail = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            fail += 1

    if fail == 0:
        print('You Lose')

    guess = input('Guess the word: ')
    guesses += guess

    if guess not in word:
        turns -= 1
        print('Try again! ')
        print(f'You have {turns} turns left...')

        if turns == 0:
            print('Fail')
            print(word)
