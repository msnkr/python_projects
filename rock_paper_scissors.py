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


answer = input('What do you chose? 0 for Rock, 1 for Paper, 2 for Scissors.')
com_choice = [rock, paper, scissors]

random_choice = random.choice(com_choice)

if answer == com_choice:
    print(f'You chose \n {answer}')
    print(f'The computer chose \n {com_choice}')

if answer == rock