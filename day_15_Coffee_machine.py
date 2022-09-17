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


def check_resources(drink):
    drink = MENU[drink]
    drink_resources = drink['ingredients']

    milk_resources = resources['milk']
    coffee_resources = resources['coffee']
    water_resources = resources['water']

    milk = drink_resources['milk']
    coffee = drink_resources['coffee']
    water = drink_resources['water']

    if milk_resources <= milk:
        print('Sorry. There is not enough Milk')
        return False
    elif water_resources <= water:
        print('Sorry. There is not enough Water')
        return False
    elif coffee_resources <= coffee:
        print('Sorry. There is not enough Coffee')
        return False
    else:
        resources['milk'] = milk_resources - milk
        resources['coffee'] = coffee_resources - coffee
        resources['water'] = water_resources - water
        return True


flag = True
while flag == True:
    drink = input('What do you want to drink?: Latte/Espresso/Cappuccino: ')
    if drink == 'report':
        for resource in resources:
            print(f'{resource}: {resources[resource]}')
    elif drink == 'off':
        flag = False
    else:
        drink = check_resources(drink)
        