from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

profit = 0
flag = True

while flag:
    menu = Menu().get_items()
    choice = input(f'What do you want to drink?: \n{menu} ')
    if choice == 'report':
        CoffeeMaker().report()
        print(profit)
    elif choice == 'off':
        flag = False 
    else:
        drink = Menu().find_drink(choice)
        cost = drink.cost
        if CoffeeMaker().is_resource_sufficient(drink):
            if MoneyMachine().make_payment(cost):
                profit += cost
                CoffeeMaker().make_coffee(drink)



