import random
import os

def play_again():
    tries = 0
    random_number = random.randint(1, 101)
    print(random_number)


    easy_hard = input('Easy or Hard Mode?: ').lower()
    if easy_hard == 'easy':
        tries = 10
    else:
        tries = 5

    flag = True
    while flag:
        pick_num = int(input('Enter Your guess: '))
        if tries == 0:
            print('You Lose. No more tries left. ')
            flag = False
        elif pick_num < random_number:
            print('Your number was too low. Try again: ')
            tries -= 1
        elif pick_num > random_number:
            print('Your number was too high. Try again: ')
            tries -= 1
        else:
            print('You got the correct number. Congrats.')
            flag = False

    if input('Do you want to go again?: ') == 'y':
        os.system('clear')
        play_again()

play_again()