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

num1 = int(input('What is the first number?: '))

for operation in operations:
    print(operation)
symbol = input('Which operator would you like to use?: ')
num2 = int(input('What is the second number?: '))

operation_symbol = operations[symbol]
answer = operation_symbol(num1, num2)

print(f'{num1} {symbol} {num2} = {answer}')

