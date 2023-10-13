############# TODO ####################

from datetime import date
from prettytable import PrettyTable
from termcolor import colored, cprint

current_date = date.today()
x = PrettyTable()
x.field_names = ["Number", "Item"]


print(current_date)
flag = True
user_list = []


def delete_list_item(todo_list):
    done_num = int(input("Which number is done? \n\n"))
    for count, item in enumerate(todo_list):
        if done_num == count+1:
            print(f"{item} is deleted")
            todo_list.remove(item)


def show_list_items(todo_list):
    x.clear_rows()
    for count, item in enumerate(todo_list):
        x.add_row([colored(count+1, "green"), colored(item, "green")])
    print(x)


while flag:
    user_input = input("Add a todo item: \n\n")
    if user_input == "show":
        show_list_items(user_list)
    elif user_input == "done":
        delete_list_item(user_list)
    elif user_input == "exit":
        flag = False
    else:
        user_list.append(user_input)
        show_list_items(user_list)
