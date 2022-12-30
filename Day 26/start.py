# List comprehension
####################################################################
# For loop.
# num_list = [1, 2, 3]
# new_num_list = []
# for n in num_list:
#     add_n = n + 1
#     new_num_list.append(add_n)

# print(new_num_list)

####################################################################

# List == list to itirate through.
# Item is each item in the list.
# New_list is code execution
# new_list = [new_item for item in list]

####################################################################


# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

####################################################################

# numbers = [1, 2, 3]
# test_list = []
# new_list = [test_list.append(n + 2) for n in numbers]

# print(test_list)

####################################################################

# List comprehension can be any sequence - Lists, tuples, Dictionaries, Strings
# name = 'Mikyle'
# new_list = [letter for letter in name]
# print(new_list)

# range_list = [number * 2 for number in range(1, 5)]
# print(range_list)

####################################################################

# Conditional list comprehension
# names = ['Mikyle', 'Kashia', 'Lara', 'Marcus', 'Selene', 'Kash', 'Angelica']
# names_list = [name for name in names if len(name) < 5]
# print(names_list)

# names = ['Mikyle', 'Lara', 'Marcus', 'Selene', 'Kash', 'Angelica']
# names_list = [name.upper() for name in names if len(name) > 5]
# print(names_list)

####################################################################

# Dictionary Comprehension
# import random
# names = ['Mikyle', 'Kashia', 'Lara', 'Marcus', 'Selene', 'Kash', 'Angelica']

# # student_dict = {key:value for item in list}
# student_dict = {name:random.randint(1, 100) for name in names}
# print(student_dict)

####################################################################

# # passed_students = {new_key:new_value for (key:value) in dict.items() if test}
# passed_students = {student:score for (student, score) in student_dict.items() if score >= 50}
# print(passed_students)

####################################################################

# Looping through dictionaries
# student_dict = {
#     'Student': ['Mikyle', 'Lara', 'Kashi'],
#     'Score': [78, 99, 98]
# }

# for (key, value) in student_dict.items():
#     print(f'{key}: {value}')

####################################################################

# Looping through items in pandas
# import pandas

# student_dict = {
#     'Student': ['Mikyle', 'Lara', 'Kashi'],
#     'Score': [78, 99, 98]
# }

# student_df = pandas.DataFrame(student_dict)
# print(student_df)
# This is not the best way.
# for (key, value) in student_df.items():
#     print(value)

####################################################################

# Loop through a dataframe
import pandas

student_dict = {
    'Student': ['Mikyle', 'Lara', 'Kashi'],
    'Score': [78, 99, 98]
}
student_df = pandas.DataFrame(student_dict)
# print(student_df)
for (index, row) in student_df.iterrows():
    # print(row)
    # Or
    # print(row.Student)
    # And this returns a dataframe series
    if row.Student == 'Kashi':
        print(f"{row.Student}: {row.Score}")

