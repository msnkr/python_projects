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

# lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(lst[(0+27) % len(lst)]) 

print(9%26)