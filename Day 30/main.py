# File not found error
# with open('data.txt')as file:
#     file.read()

# Index error
# fruits = ['Apple', 'Orange', 'Bananas']
# print(fruits[3])

# Key error
# fruits_dict = {'Apple': 'Banana'}
# print(fruits_dict['Orange'])

# Type error
# a = 'abc'
# b = 5
# print(a + b)

# try:
#     with open('Day 30/ data.txt')as file:
#         file.read()
#         a = 'abc'
#         b = 5
#         answer = a + b
#         print(answer)
# except FileNotFoundError as error:
#     print(f'{error} does not exist')
#     with open('Day 30/ data.txt', 'w')as file:
#         file.write('It exists now')
# except TypeError:
#     a = 5
#     answer = a + b
#     print(f'a = 5. Your answer is {answer}')

# else:
#     print('No errors')

# finally:
#     print('There were errors but who cares: ')
#     raise ValueError('Because i wanted to')

height = float(input('Height?: '))
weight = int(input('Weight?: '))
if height > 3:
    raise ValueError('Humans should not be taller than 3 meters.')

bmi = weight / height ** 2
print(bmi)