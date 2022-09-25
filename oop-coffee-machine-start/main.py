from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print(Menu().get_items())
choice = input('What do you want to drink?: ')
if choice == 'report':
    CoffeeMaker().report()
elif choice == 'off':
    flag = False
else:
    drink = Menu().find_drink(choice)
    if CoffeeMaker().is_resource_sufficient(drink):
        pass
    