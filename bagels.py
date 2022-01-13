import random

num_digits = 3
max_guesses = 10


def main():
    print('I am thinking of a {}- digit number with no repeated digits. Try to guess the clues: When I say "Pico", That means One digit is correct but in the wrong position. When I say "Fermi", That means One digit is correct and in the right position. When I say "Bagels", No digit is correct. For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.'.format(num_digits))

    while True:
        secret_num = get_secret_num()
        print('I have thought of a number. You have'.format(max_guesses))

        num_guesses = 1
        while num_guesses <= max_guesses:
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print('Guess {}: '.format(num_guesses))
                guess = input('> ')

                clues = get_clues(guess, secret_num)
                print(clues)
                num_guesses += 1

                if guess == secret_num:
                    break
                if num_guesses > max_guesses:
                    print('You have run out of guesses. ')
                    print('The answer was {}.'.format(secret_num))

                    print('Do you want to play again? (Y/N)')
                    if not input('> ').lower().startswith('y'):
                        break
                print('Thanks for playing! ')


def get_secret_num():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_num = ''
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    if guess == secret_num:
        return 'You\'ve got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return 'bagles'
    else:
        clues.sort()
        return ''.join(clues)


if __name__ == '__main__':
    main()
