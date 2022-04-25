def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

calculator_art = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

def calculator():
    print(calculator_art)
    should_continue = True
    num1 = float(input('Enter the first number: '))


    while should_continue:
        for item in operations:
            print(item)
        operator = input('Select a operator: ')
        num2 = float(input('Enter the Next number: '))

        operator_symbol = operations[operator]
        answer = operator_symbol(num1, num2)
        print(f'{num1} {operator} {num2} = {answer}')
        go_again = input(f'Do you want to go again? with {answer}? Y. Start again? N. e to Exit \n').lower()

        if go_again == 'y':
            num1 = answer
        elif go_again == 'n':
            should_continue = False
            calculator()
        else:
            should_continue = False
            print('Goodbye!')


calculator()






