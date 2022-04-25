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

def first_answer():
    num1 = int(input('Enter the first number: '))
    for item in operations:
        print(item)
    operator = input('Select a operator: ')
    num2 = int(input('Enter the second number: '))

    operator_symbol = operations[operator]
    answer = operator_symbol(num1, num2)
    second_answer(answer)





