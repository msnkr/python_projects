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


def money(cost):
    print('Please insert coins. ')
    quaters = int(input('How many quaters?: '))
    dimes = int(input('How many dimes?: '))
    nickels = int(input('How many nickels?: '))
    pennies = int(input('How many pennies?: '))

    total_quaters = quaters * 0.25
    total_dimes = dimes * 0.1
    total_nickels = nickels * 0.05
    total_pennies = pennies * 0.01
    
    total = total_quaters + total_dimes + total_nickels + total_pennies
    if total > cost:
        change = total - cost
        print(f'Your change is ${round(change, 2)}')
        resources['money'] += cost
        return True
    elif total == cost:
        resources['money'] += cost
        return True
    else:
        print('There is not enough money.. Money refunded')
        return False


resources['money'] = 0
flag = True
while flag == True:
    drink = input('What do you want to drink?: Latte/Espresso/Cappuccino: ').lower()
    my_drink = drink
    if drink == 'report':
        for resource in resources:
            print(f'{resource}: {resources[resource]}')
    elif drink == 'off':
        flag = False
    else:
        if drink == 'espresso':
            MENU['espresso']['ingredients']['milk'] = 0
        cost = MENU[drink]['cost']
        drink = check_resources(drink)
        if drink == True:
            if money(cost) ==  True:
                print(f'Enjoy your {my_drink.capitalize()}')
