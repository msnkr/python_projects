import random
import math


lower = int(input('Enter Lower Bound: '))
upper = int(input('Enter Upper Bound: '))

x = random.randint(lower, upper)
print(
    f'You\'ve only {round(math.log(upper - lower + 1, 2))} chances to guess the integer.')

count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input('Guess a number: '))

    if x == guess:
        print(f'Congradulations, you did it in {count} tries.')
        break
    elif x > guess:
        print('You guessed too small.')
    elif x < guess:
        print('You guessed too high.')

    if count >= math.log(upper - lower + 1, 2):
        print(f'The number is {x}... Better luck next time. ')
