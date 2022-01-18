year = int(input('Which year do you want to check?: '))

one = year / 4
two = year / 100
three = year / 400


if one == int(one) or two == int(two) or three == int(three):
            print('Leap')
else:
    print('Not a leap year.')
