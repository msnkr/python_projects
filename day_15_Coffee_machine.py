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


def check_resources(my_drink):
    drink_ingredients = MENU[my_drink]
    ingredients = drink_ingredients['ingredients']
    milk = ingredients['milk']
    cofee = ingredients['coffee']
    water = ingredients['water']

    resources_water = resources['water']
    resoures_milk = resources['milk']
    resources_coffee = resources['coffee']

    if milk < resoures_milk and cofee < resources_coffee and water < resources_water:
        new_milk = milk - resoures_milk
        new_water = water - resources_water
        new_coffee = cofee - resources_coffee

        resources['milk'] = new_milk
        resources['coffee'] = new_coffee
        resources['water'] = new_water
        return True
    else:
        print('Not enough resources')
        return False


def check_money():
    quaters = int(input('How many quaters?: '))
    dimes = int(input('How many dimes?: '))
    nickels = int(input('How many nickels?: '))
    pennies = int(input('How many pennies?: '))

    for quater in range(quaters + 1):
        quater = quaters * 0.25
    for dime in range(dimes + 1):
        dimes = dime * 0.10
    for nickel in range(nickels + 1):
        nickels = nickel * 0.05
    for pennie in range(pennies + 1):
        pennies = pennie * 0.01

    total = quaters + dimes + nickels + pennies
    cost_price = MENU[my_drink]['cost']
    if total > cost_price:
        change = total - cost_price
        print('Making your drink. ')
        print(f'Your change is: ${change}')
        print(f'Enjoy your {my_drink}')
        return True
    elif total == cost_price:
        print('Making your drink. ')
        return True
    else:
        return False
        


flag = True
while flag == True:
    my_drink = input('What do you want to drink?: Espresso/Latte/Cappuccino?: ')
    resources_ok = check_resources(my_drink)    
    if my_drink == 'off':
        flag = False
    else:
        if resources_ok == True:
            check_money()
        else:
            flag = False
