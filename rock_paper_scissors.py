rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random


answer = int(input('What do you chose? 0 for Rock, 1 for Paper, 2 for Scissors. '))
computer_choice = random.randint(0, 2)


if answer >= 3 or answer < 0:
    print('You chose an invalid number. You Lose!')
else:
    game_images = [rock, paper, scissors]

    print('You chose:')
    print(game_images[answer])

    print('Computer chose:')
    print(game_images[computer_choice])

    if answer > computer_choice:
        print('You Win!')
    elif computer_choice == answer:
        print('It\'s a Draw!')
    elif answer == 0 and computer_choice == 1:
        print('You Lose!')
    elif computer_choice == 2 and answer == 0:
        print('You Win!')
    elif computer_choice == 2 and answer == 1:
        print('You Lose!')
    elif computer_choice == 0 and answer == 2:
        print('You Lose!')