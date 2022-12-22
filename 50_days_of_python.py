# REDO 
# Day 7 Extra Challenge
##############################################################################################
##############################################################################################


# Day 2. Convert strings to integers
# convert_add = ['1', '3', '5']
# new_list = []

# for item in convert_add:
#     new_list.append(int(item))

# print(convert_add)
# print(new_list)
# print(sum(new_list)) 

# Extra Challenge
# Write a function that takes a list of names and returns the duplicates otherwise return no duplicates

# fruits = ['apple', 'orange', 'banana', 'apple']
# numbers = ['1', '2', '2', '3']
# names = ['Yoda', 'Moses', 'Joshua', 'Mark']
# non_duplicates = []

# def check_dupliacates(list_items):
#     """Loop through items in list
#     if item not in new list then append
#     if there is an append that means there is a duplicate
#     """
#     for item in list_items:
#         if item not in non_duplicates:
#             non_duplicates.append(item)
#         else:
#             print(item)
#             return False


# check = check_dupliacates(names)
# if check != False:
#     print('There are no duplicates')

##############################################################################################
# Day 3. Write a a function that that takes a dictionary with student names and if they're in school. Must return the number of studetns in school. 

# register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}
# COUNT = 0

# def register_check(random_dict):
#     """Take a dcitionary with studnt names and attendance. Return a number of how many kids are in school"""
#     global COUNT
#     for item in random_dict:
#         if random_dict[item] == 'yes':
#             COUNT += 1
#     print(COUNT)

# register_check(register)

# Extra Challenge
# Lower Case Names - Retun tuple of all lower case names in alphabetical descending order


# names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
# lower_names = []

# for name in names:
#     if name == name.lower():
#         lower_names.append(name)

# tuple_names = tuple(lower_names)
# print(tuple_names)

##############################################################################################
# Day 4. Write a function called only_floats that takes 2 arguments. Return two if both are floats or zero is none are floats

# def only_floats(a, b):
#     """Take two arguments. If they are not int, then they are floats. Return 1"""
#     count = 0
#     if a != int(a):
#         count += 1  
#     if b != int(b):
#         count += 1
#     return count

# print(only_floats(1.3, 1.6))

# Extra Challenge
# Index of the longest word. Write a function that takes a list of strings and returns 1 for each word over 4 characters.

# words1 = ["Hate", "remorse", "vengeance"]
# words2 = ["Love", "Hate"]

# def words_index(words_list):
#     """
#     Loop over everyword in the list. If the word is longer than 4, count must plus 1. Return total of count. 
#     """
#     word_count = 0
#     count = 0
#     for word in words_list:
#         for i in word:
#             word_count += 1
#         if word_count > 4:
#             count += 1
#         word_count  = 0
#     return count

# print(words_index(words2))

##############################################################################################
# Day 5. Write a function asking for price of item and discount. Return price after discount.

# def my_discount():
#     """Input price of item, input the discount. Calculate price after discount"""
#     price = int(input('What is the price of the item?: '))
#     discount = int(input('What is the discount?: '))
#     total_price = (price / 100 * discount) - price
#     print(total_price)

# my_discount()

# Extra Challenge
# Tuple of student sex. Count how many males and females in a list. Return a list of tuples.

# students = ['Male', 'Female', 'female', 'male', 'male', 'male','female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
# student_count = []
# male = 0
# female = 0
# for student in students:
#     if student.lower() == 'male':
#         male += 1
#         male_tuple = ('Male', male)
#     else:
#         female += 1
#         female_tuple = ('Female', female)

# student_count.append(male_tuple)
# student_count.append(female_tuple)

# print(student_count)

##############################################################################################
# Day 6. Username generator. Write a function that asks for a email address and returns everything before the "a" symbol. 

# def username_generator():
#     """Ask for email. Split email into list items. Select first item on list"""
#     email = input('What is your email address?: ')
#     new_email = email.split('@')
#     print(f'Your username is {new_email[0]}')


# username_generator()

# Extra Challenge
# Zeroed. Create a function that takes a list as an argument. The first and last item on the list should be zero

# a_list = [2, 5, 7, 8, 9]

# def zeroed(a_list):
#     """
#     Replace first and last item with 0
#     """
#     a_list[0] = 0   
#     a_list[-1] = 0  
#     print(a_list)

# zeroed(a_list)

##############################################################################################
#Day 7. String Range. Write a function that takes a single argument and returns a string range seperated by dots

# def string_range(i):
#     """
#     Make a for loop and create a range from argument. Use f-string to return number with dot.
#     """
#     string_item = ''
#     for item in range(i):
#        string_item += f'{item}.'
#     print(string_item)

# string_range(7)

# Extra Challenge
# Dictionary of names. Given a list of names, return all names that start with the letter S and how many times that name is in the list. Return a dictionary.

# names = ['Joseph','Nathan', 'Sasha', 'Kelly', 'Muhammad', 'Jabulani', 'Sera', 'Patel', 'Sera']
# count = 0
# name_dict = {}

# for name in names:
#     if name.startswith('S'):
#         count += 1
#         name_dict[name] = count

    
# print(name_dict)

##############################################################################################
# Day 8. Create a function called Odd Even that takes a list as a parameter, return the difference between the largest even number and the lowest odd number.

# numbers = [1,2,4,6]

# def odd_even(a_list):
#     """
#     Store the highest even number and the lowest odd number and minus them from eachother.
#     """
#     highest_even = 0
#     lowest_ood = 100
#     for number in a_list:
#         if number % 2 == 0 and number > highest_even:
#             highest_even = number
#         if number % 2 != 0 and number < lowest_ood:
#             lowest_ood = number

#     new_number = highest_even - lowest_ood
#     print(new_number)
    
# odd_even(numbers)

# Extra Challenge
# Create a function called prime_numbers. Use a single integer as am argument. Return a list of all prime numbers upto that argument

def prime_numbers(number):
    """
   Get a range of all numbers to your argement. Append to list if number is divided by one and itself only
    """
    num_list = []
    for num in range(1, number + 1):
        if num / 1 and num % 2 != 0:
            num_list.append(num)

    print(num_list)
prime_numbers(11)