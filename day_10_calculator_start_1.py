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

should_continue = True
while should_continue:
    num1 = int(input('What is the First number?: '))
    for operator in operations:
        print(operator)
    operators = input('Choose a operator: ')
    next_num = int(input('What is the second number?: '))

    operator = operations[operators]
    answer = operator(num1, next_num)
    print(f'{num1} {operators} {next_num} = {answer}')

    again = input('Would you like to go again? ')
    if again == 'n':
        print('Goodbye!')
        should_continue = False
    next_num = int(input('What is the second number?: '))
    operators = input('Choose a operator: ')
    new_answer = operator(answer, next_num)

    
    print(f'{answer} {operators} {next_num} = {new_answer}')
