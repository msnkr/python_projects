# Renaming Variables


# a = input('a: ')
# b = input('b: ')

# c = a
# a = b
# b = c

# print('a= ' + a)
# print('b= ' + b)


# fname = input('First Name: ')
# lname = input('Last Name: ')

# name = fname
# fname = lname
# lname = name

# print(fname, lname)


# city = input('Whats the name of the city you grew up in? \n')
# pet_name = input('What is the name of your pet? \n')

# v = city
# city = pet_name
# pet_name = v

# print(f'Your bands name is: {city} {pet_name}')


# Use type when getting str and int errors

# two_digit_number = input('Enter a two digit number: ')
# a = int(two_digit_number[0])
# b = int(two_digit_number[1])

# print(a + b)

# print(3 * 3 + 3 / 3 - 3)
# print(3 * (3 + 3) / 3 - 3)

# height = int(input('What is your height?: '))
# price = 0

# Greater than >
# Less than <

# if height >= 120:
#     age = int(input('How old are you?: '))
#     if age <= 12:
#         price += 5
#     elif age < 18:
#         price += 7
#     elif age >= 45 and age <= 55:
#         price == 0
#     else:
#         price += 12
#     wants_photo = input('Do you want a photo?: y/n ')
#     if wants_photo == 'y':
#         price += 3

#     print(f'${price}')
# else:
#     print('You are not tall enough to ride this attraction. ')

# remember!!! 9 > 3 and 5 < 9
# if age is 45 then
# if age < 18:
#   print('Free') etc

# import random

# # rand_int = random.randint(0, 5)
# # print(rand_int)

# rand_float = random.random() * 5
# print(round(rand_float,2))

# import random

# heads = 1
# tails = 0

# choice = random.randint(0, 1)

# if choice == 1:
#     print('Heads')
# elif choice == 0:
#     print('Tails')

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)


# def hello_world(greeting, name):
#     print(greeting, name)

# hello_world('Hello', 'Mikyle')

# x = 0

# while x < 10:
#     print(x)
#     x+=1
#     if x == 5:
#         print('Your at 5')
# print('Done')

# lst = ['apples', 'bananas', 'grapes']

# should_contine = True
# while should_contine:
#     for item in lst:
#         print(item)
#         if item == 'bananas':
#             print('Stop here')
#             should_contine = False

# lst = ['a', 'b', 'b', 'c', 'd', 'e', 'e', 'e', 'f', 'g']
# letters = ''

# should_continue = True
# while should_continue:
#     for i in lst:
#         if i == 'f':
#             should_continue = False
#             letters += '. F is supposed to be here. '
#             break
#         else:
#             letters += i


# print(letters)

# num = 0

# while num < 10:
#     num += 1
#     print(num)


# lst = ['a', 'b', 'b', 'c', 'd', 'e', 'e', 'e', 'f', 'g']
# print(lst)

# for item in range(len(lst)):
#     letter = lst[item]
#     if letter == 'e':
#         lst[item] = 'changed'

# print(lst)

# phones = ['samsung', 'huawei', 'iPhone', 'LG']

# for item in range(len(phones)):
#     if phones[item] == 'iPhone':
#         phones[item] = 'motorola'

# print(phones)


# lst = ['a', 'b', 'c', 'c', 'd', 'e', 'f', 'f']

# for item in range(len(lst)):
#     if lst[item] == 'd':
#         lst[item] = 'changed'
# print(lst)

# def greet(name):
#     print(f'Hello {name}')
#     print(f'How are you, {name}? ')

# greet('Mikyle')

# Keyword arguments
# def greet_with(name, location):
#     print(f'Hello {name}.')
#     print(f'What is it like in {location}? ')

# # This is a keyword argument => Name and location
# greet_with(location='Johannesburg', name='Mikyle')


# num = 5
# if num % 1 == 0 and num % 2 != 0:
#     print('prime')

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# # print(alphabet[(0+27) % len(alphabet)])


# def caesar(direction, text, shift):
#     empty_var = ''
#     for number in text:
#         if number in alphabet:
#             if direction == 'decode':
#                 position = alphabet.index(number) - shift
#             else:
#                 position = alphabet.index(number) + shift
#             new_item = alphabet[position]
#             empty_var += new_item
#         else:
#             empty_var += number
#     print(f'Your {direction}d word is: {empty_var}')


# should_contine = True
# while should_contine:
#     direction = input('Encode or Decode? \n')
#     text = input('Enter your text \n')
#     shift = int(input('Shift amount \n'))


#     caesar(direction, text, shift)

#     answer = input('Continue? Y/N \n').lower()
#     if answer == 'n':
#         should_contine = False
#         print('Goodbye')


# Dictionaries
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again."
#     }

# Retrieving items in dictionary
# print(programming_dictionary['Function'])

# Adding new item to dictionary
# programming_dictionary['Loop'] = 'The action of doing something over and over again.'


# Creating and wiping dictionary
# new_dictionary = {}

# Edit existing or create a new item in dictionary
# programming_dictionary['Bug'] = 'A moth in your computer.'
# print(programming_dictionary['Bug'])


# Loop through key value in dictionary
# for key in programming_dictionary:
#     print(f'{key}: {programming_dictionary[key]}')

#     This selects each key and value from dictionary


# Nesting
# capitals = {
#     'France': 'Paris',
#     'Germany': 'Berlin'
# }

# Nesting a list in a dictionary
# travel_log = {
#     'France': ['Paris', 'Lille', 'Dijon'],
#     'Germany': ['Berlin', 'Hamburg', 'Stuttgart']
# }

# Nest dictionary in a dictionary
# travel_log = {
#     'France': {
#         'cities_visited': ['Paris', 'Lille', 'Dijon'],
#         'total_visits': 12
#         },
#     'Germany': {'cities_visited': ['Germany', 'Hamburg', 'Stuttgart'], 'times_visited': 12}
# }

# print(travel_log['Germany'])

# Nesting dictionary in a list

# travel_log = [
#     {
#         'country': 'France',
#         'cities_visited': ['Paris', 'Lille', 'Dijon'],
#         'times_visited': 12
#     },
#     {
#     'country': 'Germany',
#     'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
#     'times_visited': 14
#     }
# ]

# print(travel_log[1]['country'])

# should_continue = True
# bio = {}


# def calculate(bid):
#     oldest = 0
#     name_of_oldest = ''
#     for key in bio:
#         if bio[key] > oldest:
#             oldest = bio[key]
#             name_of_oldest = key

#     print(f'The oldest person is {name_of_oldest} at age: {oldest}')


# while should_continue:
#     name = input('What is yor name?: ')
#     age = int(input('How old are you?: '))

#     bio[name] = age

#     go_again = input('Do you want to go again? Y/N \n').lower()
#     if go_again == 'n':
#         should_continue = False
#         calculate(bio)


# Functions with outputs
# def format_name(first, last):
#     return f'{first.title()} {last.title()}'

# print(format_name('mikyle', 'kruger'))

# f_name = input('What is your first name? ')
# l_name = input('What is your last name? ')

# def format_name(f_name, l_name):
#     # Docstring is to give your function an explanation of what it does.
#     """
#     Takes first name and last name input and returns title case.
#     If no first or last name, return none
#     """
#     if f_name == '' and l_name == '':
#         # This will return None
#         return 'Nothing was added'
#     return f'{f_name.title()} {l_name.title()}'

# Must use print statement else it won't return anything.
# print(format_name(f_name, l_name))

# lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# new_dict = {}

# for num in range(len(lst)):
#     for letter in lst[num]:
#         new_dict[num] = letter

# print(new_dict)

# lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# for item in range(len(lst)):
#     letter = lst[item]
#     if letter == 'c':
#         lst[item] = 'Changed'

# print(lst)

# birthday_dict = {
#     'mikyle': '26 October',
#     'kashia': '17 November',
#     'lara': '26 February',
# }


# def add(num1, num2):
#     return num1 + num2

# def subtract(num1, num2):
#     return num1 - num2

# def divide(num1, num2):
#     return num1 / num2

# def multiply(num1, num2):
#     return num1 * num2

# symbol_operators = {
#     '+': add,
#     '-': subtract,
#     '/': divide,
#     '*': multiply
# }


# def calculate():
#     num1 = int(input('What is the first number?: '))
#     should_continue = True

#     while should_continue:
#         for item in symbol_operators:
#             print(item)
#         operators = input('Choose your operator: ')
#         num2 = int(input('What is the next number?: '))

#         operator = symbol_operators[operators]
#         answer = operator(num1, num2)

#         print(f'{num1} {operators} {num2} = {answer}')
#         go_again = input(f'Would you like to continue from {answer}? Or start again? Or Exit?: ')

#         if go_again == 'y':
#             num1 = answer
#             should_continue = True
#         elif go_again == 'n':
#             should_continue = False
#             calculate()
#         else:
#             should_continue = False
#             print('Goodbye!')

# calculate()


# lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# new_lst = []

# for item in lst:
#     if item == 'c':
#         new_lst.append('changed')
#     new_lst.append(item)

# print(new_lst)

# lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for item in range(len(lst)):
#     letter = lst[item]
#     if letter == 'c':
#         lst[item] = 'changed'


# print(lst)


# def get_name():
#     birthdays_dict = {}
#     birthday_name = ''
#     birday_age = 0
#     should_continue = True


#     while should_continue:
#         name = input('What is their name?: ')
#         age = int(input('What is their age?: '))
#         birthdays_dict[name] = age

#         another_name = input('Do you want to add another person?: Start again send "s": \n')
#         if another_name == 'n':
#             should_continue = False

#             for item in birthdays_dict:
#                 bday_age = birthdays_dict[item]
#                 if birday_age < bday_age:
#                     birday_age = bday_age
#                     birthday_name = item
#             print(f'{birthday_name} is the eldest at {birday_age} years old!')

#         elif another_name == 's':
#             should_continue = False
#             get_name()

# get_name()


# def calculate_age(new_dict):
#     new_age = 0
#     new_name = ''

#     for item in new_dict:
#         if new_dict[item] > new_age:
#             new_age = new_dict[item]
#             new_name = item
#     print(f'The eldest is {new_name.capitalize()} at {new_age} ')

# # empty dictionary
# my_dict = {}
# should_contine = True
# while should_contine:
#     # input name and age
#     name = input('What is the name: ')
#     age = int(input('How old are they?: '))
#     # save to dictionary
#     my_dict[name] = age
#     # ask if theres more names
#     go_again = input('Would you like to add another entry?: ')
#     if go_again == 'n':
#         calculate_age(my_dict)
#         should_contine = False
#     # if not then calculate the eldest


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# for letter in range(len(alphabet)):
#     # returns individual numbers
#     item = alphabet[letter]
#     # prints the actual letters of each number
#     if item == 'd':
#         alphabet[letter] = 'changed'
#         # alphabet and number change

# print(alphabet)

# ###############################################################################################################################################################

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# for item in alphabet:
#     print(item, end=' ')
#     End removes the escape character and replaces it with ' ' or /. You can put anything to replace the escape character

# seperator replaces the escape character too
# print('19', '12', '1990', sep='/')

# Merge Dictionaries
# name1 = {
#     'kelly': 23,
#     'Raju': 22,
#     'Derrick': 24,
#     'John': 19
# }

# name2 = {
#     'Ravi': 25,
#     'Mpho': 22
# }

# # Method 1
# # print(name1 | name2)

# #Method 2
# name = {**name1, **name2 }
# print(name)

# Caldender with Python
# import calendar

# month = calendar.month(2022, 8)
# print(month)

# Get Current time with python
# from datetime import datetime

# time_now = datetime.now().strftime('%H:%M:%S')
# print('The current time is ' + time_now)

# Sort a list in descending order
# list = [2, 7, 5, 4, 3, 6, 1]
# list.sort(reverse=True)
# # You can't use the sort method to create a new object. Sort is strictly a list method

# print(list)


# Swapping variables
# x, y = 20, 30
# x, y = y, x
# print(x, y)


# Count how many items in a list
# names = ['mikyle', 'kashia', 'lara', 'marcus', 'lara', 'simone', 'lara']

# count = 0

# for item in names:
#     if item == 'lara':
#         count += 1

# print(f'The name appears {count} times.')


# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo


# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.

# import random
# import os

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
# def compare(user_score, computer_score):
#     if user_score == computer_score:
#         return 'It\'s a draw'
#     elif computer_score == 0:
#         return 'Computer wins with blackjack.'
#     elif user_score == 0:
#         return 'You win. You got a blackjack'
#     elif user_score > 21:
#         return 'You Lose. You drew over 21'
#     elif computer_score > 21:
#         return 'You win. Computer drew over 21.'
#     elif user_score > computer_score:
#         return 'You win. You drew higher than the computer.'
#     else:
#         return 'You lose. The computer drew higher than you.'


# #Hint 6: Create a function called calculate_score() that takes a List of cards as input
# #and returns the score.
# #Look up the sum() function to help you do this.
# def calculate_score(cards):
#     """Return sum of score if not blackjack or over 21"""
#     #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#     if len(cards) == 2 and sum(cards) == 21:
#         return 0
#     #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove()
#     elif sum(cards) > 21 and 11 in cards:
#         cards.remove(11)
#         cards.append(1)
#         return sum(cards)
#     return sum(cards)

# def deal_card():
#     """Return a random card"""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     return random.choice(cards)


# def play_game():
#     user_cards = []
#     computer_cards = []


#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())


#     is_game_over = False
#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#         print(f'Your cards are: {user_cards}. Total score: {user_score}')
#         print(f'Computers first card: {computer_cards[0]}')
#         #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True

#         #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
#         elif input(('Do you want to draw another card?: ')) == 'y':
#             user_cards.append(deal_card())
#         else:
#             is_game_over = True


#         #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)
#         """Must use computer score else it will go in a for loop because it will use the old score and never actually change"""

#     print(compare(user_score, computer_score))


# #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo
# if input('Do you want to play a game of blackjack   a?: ') == 'y':
#     os.system('clear')
#     play_game()


# ###################################scope#######################################

# enemies = 1

# def inside_enemies():
#     enemies = 2
#     print(f'How many enemies?: {enemies}')

# inside_enemies()
# print(f'How many enemies now?: {enemies}')


# ####################


# turns = 10

# def new_turns():
#     return turns - 1

# while turns != 0:
#     turns = new_turns()

#     if turns == 0:
#         print('It is now 0')
#     else:
#         print(turns)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'{self.name} {self.age}'

# x = Person('John', 36)
# y = Person('Lara', 16)
# print(x)
# print(y)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# print(p1)
# p1.myfunc()

# class Person:
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age

#     def myfunc(abc):
#         print(f'My name is {abc.name}')

# p1 = Person('john', 36)
# p1.myfunc()
# p1.name = 'Mikyle'
# p1.age = 40
# print(p1.name)
# print(p1.age)


# class User:
#     def __init__(self, user_id, username):
#         self.user_id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0


#     def follow(self, user):
#         user.followers += 1
#         self.following += 1

# user_1 = User('001', 'mikyle')
# user_2 = User('002', 'Lara')
# print(user_1.followers)
# print(user_2.user_id)

# user_1 = User('001', 'mikyle')
# user_2 = User('002', 'Lara')

# user_1.follow(user_2)
# print(f'{user_1.username} is following {user_1.following} user.')
# print(f'{user_2.username} is being followed by {user_2.followers} user.')


# class UserDatabase:

#     def __init__(self, username, age, pay):
#         self.username = username
#         self.age = age
#         self.pay = pay


#     def deduct(self):
#         taxes = self.pay / 18 * 100 # This is wrong but whatevs
#         return taxes


#     def __str__(self):
#         return f'Name: {self.username.capitalize()} | Age: {self.age} | Pay: {self.deduct()}'


# user = UserDatabase('mikyle', 30, 50000)
# print(user)


# class CarBluePrint:

#     def __init__(self, make, color):
#         self.make = make
#         self.color = color
#         self.speed = 0


#     def start(self):
#         self.speed += 60


#     def stop(self):
#         self.speed = 0


#     def PrintMakeAndColor(self):
#         print(f'{self.make}: {self.color} : {self.speed}')


# toyota = CarBluePrint('toyota', 'white')
# toyota.start()
# print(toyota.speed)

# toyota.stop()
# print(toyota.speed)

# vw = CarBluePrint('Volkswagen', 'red')
# vw.start()
# print(vw.speed)
# vw.stop()
# print(vw.speed)

# vw.PrintMakeAndColor()

# from turtle import Screen
# from day_18_start import RandomWalk

# diagrams = RandomWalk()
# diagrams.call_diagrams()
# diagrams.random_walk(150)
# my_screen = Screen()
# my_screen.exitonclick()


# class User:

#     def __init__(self, username):
#         self.username = username
#         self.followers = 0
#         self.following = 0


#     def follow(self, username):
#         self.following += 1
#         username.followers += 1 # If it was self.followers then the user would follow themselves


#     def __str__(self):
#         return f'{self.username} is following {self.following} users and being followed by {self.followers}'


# user_1 = User('mikyle')
# user_2 = User('lara')

# user_1.follow(user_2)

# print(user_1)
# print(user_2)

# from turtle import Turtle, Screen
# import random


# def random_colors():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colors = (r, g, b)
#     return colors


# tim = Turtle()
# tim.speed(7)
# Screen().colormode(255)


# def draw(gap):
#     angle = int(360 / gap)
#     for _ in range(angle):
#         tim.color(random_colors())
#         tim.circle(50)
#         tim.setheading(tim.heading() + gap)

# draw(10)

# Screen().exitonclick()


# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def w():
#     tim.setheading(90)
#     tim.forward(50)


# def a():
#     tim.setheading(180)
#     tim.forward(50)


# def s():
#     tim.setheading(270)
#     tim.forward(50)


# def d():
#     tim.setheading(0)
#     tim.forward(50)


# screen.onkeypress(a, 'a')
# screen.onkeypress(w, 'w')
# screen.onkeypress(d, 'd')
# screen.onkeypress(s, 's')

# screen.listen()
# screen.exitonclick()


# Higher order functions

# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# def calculate(n1, n2, func):
#     return func(n1, n2)


# result = calculate(5, 5, subtract)
# print(result)


# from turtle import Turtle, Screen
# import random


# screen = Screen()
# colors = ['red', 'yellow', 'orange', 'green', 'blue', 'purple']
# y_positions = [-100, -50, -0, 50, 100, 150]
# turtles = []

# for x in range(6):
#     turtle = Turtle(shape='turtle')
#     turtle.speed(0)
#     turtle.penup()
#     turtle.color(colors[x])
#     turtle.goto(-460, y_positions[x])
#     turtles.append(turtle)

# race_on = True
# while race_on:
#     for turtle in turtles:
#         random_speed = random.randint(0, 10)
#         turtle.forward(random_speed)

#         if turtle.xcor() > 460:
#             winner = turtle.pencolor()
#             print(f'{winner}')
#             race_on = False

# screen.exitonclick()


# from turtle import Turtle, Screen

# screen = Screen()
# screen.bgcolor('black')
# screen.title('This is your snake game')
# coordinates = [(0, 0), (-20, 0), (-40, 0)]

# for x in coordinates:
#     snake = Turtle(shape='square')
#     snake.color('white')
#     snake.goto(coordinates)


# screen.exitonclick()


# Class inheritance
# class Animal:
#     def __init__(self):
#         self.eyes = 2

#     def breath(self):
#         print('Inhale and exhale')


# class Fish(Animal):
#     def __init__(self):
#         super().__init__()


#     def breath(self):
#         super().breath()
#         print('Under water')


#     def swim(self):
#         print('Swims underwater')


# nemo = Fish()
# nemo.breath()


# my_list = ['a', 'b', 'c', 'd', 'e', 'f']

# print(my_list[0:1:-1])

#### PANDAS ####
# import pandas

# gray = 0
# black = 0
# cinnamon = 0

# pd = pandas.read_csv('python_projects/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# for row in pd['Tail twitches']:
#     if row == True:
#         s_id = pd['Primary Fur Color']

# for row in s_id:
#     if row == 'Gray':
#         gray += 1
#     elif row == 'Black':
#         black += 1
#     else:
#         cinnamon += 1

# print(f'Gray: {gray} \nBlack: {black} \nCinnamon: {cinnamon}')
# print(pd.columns)

# import pandas


# pd = pandas.read_csv('Day 25/Us States Start/50_states.csv')


# guess = input('Guess a state: ').title()
# for row in pd.state:
#     if guess == row:
#         state = pd[pd.state == guess]

#         state_x = state.x
#         state_y = state.y

# print(state)
# print(state_x)
# print(state_y)

############## TODO ####################

# from datetime import date
# from prettytable import PrettyTable
# from termcolor import colored, cprint

# current_date = date.today()
# x = PrettyTable()
# x.field_names = ["Number", "Item"]


# print(current_date)
# flag = True
# user_list = []


# def delete_list_item(todo_list):
#     done_num = int(input("Which number is done? \n\n"))
#     for count, item in enumerate(todo_list):
#         if done_num == count+1:
#             print(f"{item} is deleted")
#             todo_list.remove(item)


# def show_list_items(todo_list):
#     x.clear_rows()
#     for count, item in enumerate(todo_list):
#         x.add_row([colored(count+1, "green"), colored(item, "green")])
#     print(x)


# while flag:
#     user_input = input("Add a todo item: \n\n")
#     if user_input == "show":
#         show_list_items(user_list)
#     elif user_input == "done":
#         delete_list_item(user_list)
#     elif user_input == "exit":
#         flag = False
#     else:
#         user_list.append(user_input)
#         show_list_items(user_list)

############## Calculator ####################


# def add(num1, num2):
#     return num1 + num2


# def subtract(num1, num2):
#     return num1 - num2


# def multiply(num1, num2):
#     return num1 * num2


# def divide(num1, num2):
#     return num1 / num2


# question = input("What do you want to do? \n\n")


# for letter in question:
#     if letter == " ":
#         pass
#     else:
#         num1 = int(question[0])
#         num2 = int(question[-1])
#         if letter == "+":
#             print(add(num1, num2))
#         elif letter == "-":
#             print(subtract(num1, num2))
#         elif letter == "*":
#             print(multiply(num1, num2))
#         elif letter == "/":
#             print(divide(num1, num2))


############## Guess the number ####################
# from random import randint

# tries = 10
# random_num = randint(0, 100)
# flag = True

# while flag:
#     guess = int(input("Guess the number between 0 and 100 \n"))
#     print(f"You have {tries} left")
#     if tries == 0:
#         flag = False
#     else:
#         if guess == random_num:
#             print("Just right")
#             flag = False
#         elif guess < random_num:
#             print("Too low")
#             tries -= 1
#         else:
#             print("too high")
#             tries -= 1

############## Password Generator ####################
# import random

# characters = list(
#     "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~")


# random_pass = ""
# get_digits = int(input("How many: "))
# for letter in range(get_digits):
#     random_letter = random.choice(characters)
#     random_pass += random_letter


# print(random_pass)


############## Expense Tracker ####################
# from prettytable import PrettyTable

# x = PrettyTable()

# print("Welcome to Expense Tracker")
# print("Add item: {add}")
# print("Add income: {income}")
# print("List items and money: {list}")
# print("Remaining money: {remain}")
# print("Save list: {save}")
# print("Delete list item: {delete}")
# print("Exit: {exit}")

# bills = {}
# total_expense = 0
# my_income = 0


# def delete_item(bills):
#     for count, item in enumerate(bills):
#         print(count, item)
#     delete = input("Which item do you want to delete?: ")


# def list_bills(bills):
#     x.clear()
#     x.field_names = ["Bill", "Money"]
#     for bill_item in bills:
#         bill_name = bill_item
#         bill_amount = bills[bill_item]
#         x.add_row([bill_name, bill_amount])
#     print(x)
#     if my_income == 0:
#         print(f"Your total expense is {total_expense}")
#     else:
#         print(
#             f"Your total expense is {total_expense}. Your income is {my_income}. You're left with {income - total_expense}")


# flag = True
# while flag:
#     todo = input("What do you want to do? ")
#     if todo == "exit":
#         flag = False
#     elif todo == "income":
#         income = int(input("Add income: "))
#         my_income += income
#     elif todo == "delete":
#         delete_item(bills)
#     elif todo == "add":
#         name_expense = input("What do you want to add?: ")
#         money_expense = int(input("How much?: "))
#         total_expense += money_expense
#         bills[name_expense] = money_expense
#     elif todo == "list":
#         list_bills(bills)


# import tkinter as tk

# BACKGROUND_COLOR = "#445069"
# BUTTON_COLOR = "#5B9A8B"
# FOREGROUNF_COLOR = "#F7E987"

# root = tk.Tk()
# root.title("Hello")

# root.configure(background=BACKGROUND_COLOR, width=300,
#                height=400, padx=10, pady=10)


# def say_hello():
#     label.configure(text="Updated text")


# label = tk.Label(root, text="Hello There")
# label.grid(row=0, columnspan=3, pady=8)
# label.config(bg=BACKGROUND_COLOR, fg=FOREGROUNF_COLOR)

# quit_btn = tk.Button(
#     root, text="Quit", command=root.destroy)
# quit_btn.grid(row=1, column=1)
# quit_btn.config(background=BUTTON_COLOR,
#                 fg=FOREGROUNF_COLOR, highlightthickness=0)

# function_btn = tk.Button(root, text="Click me",
#                          command=say_hello)
# function_btn.grid(row=1, column=2, padx=4)
# function_btn.config(background=BUTTON_COLOR,
#                     fg=FOREGROUNF_COLOR, highlightthickness=0)

# root.mainloop()

import tkinter as tk

window = tk.Tk()


def get_user_input():
    user_input = name_entry.get()
    label.config(text=user_input)


window.title("Testing")
window.config(background="black", padx=10, pady=10)
window.grid()

label = tk.Label(window, text="Enter your name: ")
label.grid(columnspan=2, row=0, padx=4, pady=4)
label.config(background="black", foreground="white")

name_entry = tk.Entry(window)
name_entry.grid(columnspan=2, row=1, padx=2, pady=2)

quit_btn = tk.Button(window, text="Quit", command=window.destroy)
quit_btn.grid(column=0, row=2, padx=4, pady=4)
submit_btn = tk.Button(window, text="Submit", command=get_user_input)
submit_btn.grid(column=1, row=2, padx=4, pady=4)

window.mainloop()
