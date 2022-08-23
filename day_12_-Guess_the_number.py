# import random
# import os

# def play_again():
#     tries = 0
#     random_number = random.randint(1, 101)
#     print(random_number)


#     easy_hard = input('Easy or Hard Mode?: ').lower()
#     if easy_hard == 'easy' or 'e':
#         tries = 10
#     else:
#         tries = 5

#     flag = True
#     while flag:
#         pick_num = int(input('Enter Your guess: '))
#         if tries == 0:
#             print('You Lose. No more tries left. ')
#             flag = False
#         elif pick_num < random_number:
#             print('Your number was too low. Try again: ')
#             tries -= 1
#         elif pick_num > random_number:
#             print('Your number was too high. Try again: ')
#             tries -= 1
#         else:
#             print('You got the correct number. Congrats.')
#             flag = False

#     if input('Do you want to go again?: ') == 'y':
#         os.system('clear')
#         play_again()

# play_again()

###################3 Her KAK VERSION ########################

# from random import randint

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()


############################### Try 2
import random


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0


def compare(answer, guess, turns):
  if guess < answer:
    print('You are too low.')
    return turns -1
  elif guess > answer:
    print('You are too high.')
    return turns -1
  else:
    print('You are correct. Well Done. You win.')


def set_difficulty():
  difficulty = input('Easy or hard game?: ')
  if difficulty == 'easy':
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  turns = set_difficulty()
  answer = random.randint(1, 100)
  guess = 0



  while guess != answer:
    print(f'You have {turns} turns left. ')
    guess = int(input('What is your guess?: '))
    turns = compare(answer, guess, turns)

    if turns == 0:
      print('You have run out of turns. ou Lose.')
      break
    elif guess != answer:
      print('Try again!')


  if input('Do you want to play again?: ') == 'y':
    game()

game()
  



