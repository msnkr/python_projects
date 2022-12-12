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


choice = int(input('What do you choose?: 0 for ROCK, 1 for PAPER, 2 for SCISSORS \n'))
computer_choice = random.randint(0, 2)

images = [rock, paper, scissors]
if choice >= 3 or choice < 0:
    print('You chose an invalid number. You Lose!')
else:
    print('You Chose:')
    print(images[choice])

    print('You Chose:')
    print(images[computer_choice])

    if choice == computer_choice:
        print('It\'s a Draw.')
    elif choice == 2 and computer_choice == 0:
        print('You Lose')
    elif choice > computer_choice:
        print('You Win')
    elif choice == 0 and computer_choice == 2:
        print('You Win')
    elif choice == 1 and computer_choice == 0:
        print('You Win')
    elif choice == 1 and computer_choice == 2:
        print('You Lose')
    elif choice == 0 and computer_choice == 1:
        print('You Lose')
