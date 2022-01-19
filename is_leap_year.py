year = int(input('Which year do you want to check?: '))

# one = year / 4
# two = year / 100
# three = year / 400


# if one == int(one) or two == int(two) or three == int(three):
#     print('Leap Year')
# else:
#     print('Not a leap year.')
if year % 4 == 0:
    if year % 100 != 0:
        print('Leap Year')
    elif year % 400 == 0:
        print('Leap Year')
    else:
        print('Not a leap year')
else:
    print('Not leap year.')
