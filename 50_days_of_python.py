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

    