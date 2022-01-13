import random

num_digits = 3
max_guesses = 10


def main():
    print(f'I am thinking of a {format(num_digits)}- digit number with no repeated digits. Try to guess the clues: When I say "Pico", That means One digit is correct but in the wrong position. When I say "Fermi", That means One digit is correct and in the right position. When I say "Bagels", No digit is correct. For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.')

    while True:
        secretNum = getSecretNum()
        print('I have thought of a number. ')
        print(f'You have {format(max_guesses)} guess left.')

        numGuesses = 1
        while numGuesses <= max_guesses:
            guess = ''
            while len(guess) != num_digits or guess.isdecimal():
                print(f'Guess: {format(numGuesses)}')
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > max_guesses:
                print('You have run out of guesses')
                print(f'The correct answer is: {format(secretNum)}')

            print('Do you want to play again? (Y/N)')
            if not input('> ').lower().startswith('y'):
                break
            print('Thanks for playing.')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(num_digits):
        secretNum += str(numbers[i])
        return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] == secretNum:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagel'
    else:
        clues.sort()
        return ''.join(clues)


if __name__ == '__main__':
    main()
