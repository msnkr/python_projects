MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def pay_now(cost):
    quaters = int(input('How many qauters?: '))
    for item in range(quaters + 1):
        quaters = item * 0.25

    dimes = int(input('How many dimes?: '))
    for item in range(dimes + 1):
        dimes = item * 0.10

    nickels = int(input('How many nickels?: '))
    for item in range(nickels + 1):
        nickels = item * 0.5

    pennies = int(input('How many pennies?: '))
    for item in range(pennies + 1):
        pennies = item * 0.1

    return f"quaters{quaters} dimes{dimes} + nickels{nickels} + pennies{pennies}"


def is_enough(my_drink):
    my_drink = MENU[my_drink]
    drink_resources = my_drink['ingredients']
    
    if my_drink != 'espresso':
        drink_milk = drink_resources['milk']
        drink_water = drink_resources['water']
        drink_coffee = drink_resources['coffee']
    
    if drink_coffee < resources['coffee'] and drink_milk < resources['milk'] and drink_water < resources['water']:
        return my_drink['cost']


my_drink = input('What do you want to drink?: Espresso/Latte/Capaccino ')

if my_drink == 'report':
    for _ in resources:
        print(f'The current resources are: {_}: {resources[_]}')

cost = is_enough(my_drink)
print(pay_now(cost))