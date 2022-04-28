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

    #This selects each key and value from dictionary


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

# def add(n1, n2):
#     return n1 + n2


# def subtract(n1, n2):
#     return n1 - n2


# def multiply(n1, n2):
#     return n1 * n2


# def divide(n1, n2):
#     return n1 / n2


# operators = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide
# }    


# def calculate():
#     should_continue = True

#     number1 = int(input('Enter the first number: '))
#     while should_continue:
#         for item in operators:
#             print(item)
#         symbol = input('Which operator would you like to use?: ')
#         number2 = int(input('Enter the second number: '))

#         calculation = operators[symbol]
#         answser = calculation(number1, number2)
#         print(answser)
#         go_again = input(f'Continue with {answser}? Y. Start again? N. E to exit.').lower()
#         if go_again == 'y':
#             number1 = answser
#         elif go_again == 'n':
#             should_continue = False
#             calculate()
#         else:
#             should_continue = False
#             print('Goodbye')

# calculate()

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for item in range(len(lst)):
    letter = lst[item]
    if letter == 'g':
        lst[item] = 'changed'
print(lst)