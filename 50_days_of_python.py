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

def my_discount():
    """Input price of item, input the discount. Calculate price after discount"""
    pass