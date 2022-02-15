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


answer = input('What do you chose? 0 for Rock, 1 for Paper, 2 for Scissors. ')

if answer == 0:
    answer = rock
elif answer == 1:
    answer = paper
elif answer == 2:
    answer = scissors

com_choice = [rock, paper, scissors]
random_choice = random.choice(com_choice)


print(answer)
print()
print()
print()
print()
print(random_choice)

# if answer == random_choice:
#     print(f'You chose \n {answer}! ')
#     print(f'computer chose \n {random_choice}! ')
#     print('Draw!')