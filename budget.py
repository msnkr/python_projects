budget = {}


def budget_input():
    name = input('Name: ').lower()
    money = int(input('Amount: '))
    budget[name] = money



start = True
while start:
    budget_input()
    go_again = input('Add Another Amount: (Y/N) ')
    if go_again == 'n':
        break
    elif go_again == 'l':
        for name in budget:
            print(f'You currently have \n\t{name}')

total = 0
for x in budget:
    total += budget[x]

print(f'Your total amount is: {total}')
add_salary = input('Do you want to deduct it from your salary?: (Y/N) ')
if add_salary == 'y':
    salary = int(input('What is your salary?: '))
    total = salary - total
    print(f'Your total take home is: {total}')

with open('budget.txt', 'w') as f:
    for item in budget:
        f.write(f'{item}: {budget[item]}\n')