from prettytable import PrettyTable
from prettytable.colortable import ColorTable

x = PrettyTable()
# x = ColorTable(theme=Themes.OCEAN)
x.field_names = ['Name:', 'Money:']


budget = {}
def budget_input():
    name = input('Name: ').lower()
    money = int(input('Amount: '))
    budget[name] = money


go_again = True
while go_again:
    budget_input()
    answer = input('Add Another?: ')
    if answer == 'y':
        budget_input()
    elif answer == 'l':
        for item in budget:
            x.add_row([item, budget[item]])
            print(x)
    else:
        break

total = 0
for item in budget:
    total += budget[item]
    x.add_row([item, budget[item]])

print(x)

# print(f'Your total bills amount to: {total}')
# add_salary = input('Do you want to deduct it from your salary?: (Y/N) ')
# if add_salary == 'y':
#     salary = int(input('What is your salary?: '))
#     total = salary - total
#     print(f'Your total take home is: {total}')


# with open('budget.txt', 'w') as f:
#     for item in budget:
#         f.write()