############# Expense Tracker ####################
from prettytable import PrettyTable

x = PrettyTable()

print("Welcome to Expense Tracker")
print("Add item: {add}")
print("Add income: {income}")
print("List items and money: {list}")
print("Remaining money: {remain}")
print("Save list: {save}")
print("Delete list item: {delete}")
print("Exit: {exit}")

bills = {}
total_expense = 0
my_income = 0


def delete_item(bills):
    for count, item in enumerate(bills):
        print(count, item)
    delete = input("Which item do you want to delete?: ")


def list_bills(bills):
    x.clear()
    x.field_names = ["Bill", "Money"]
    for bill_item in bills:
        bill_name = bill_item
        bill_amount = bills[bill_item]
        x.add_row([bill_name, bill_amount])
    print(x)
    if my_income == 0:
        print(f"Your total expense is {total_expense}")
    else:
        print(
            f"Your total expense is {total_expense}. Your income is {my_income}. You're left with {income - total_expense}")


flag = True
while flag:
    todo = input("What do you want to do? ")
    if todo == "exit":
        flag = False
    elif todo == "income":
        income = int(input("Add income: "))
        my_income += income
    elif todo == "delete":
        delete_item(bills)
    elif todo == "add":
        name_expense = input("What do you want to add?: ")
        money_expense = int(input("How much?: "))
        total_expense += money_expense
        bills[name_expense] = money_expense
    elif todo == "list":
        list_bills(bills)
