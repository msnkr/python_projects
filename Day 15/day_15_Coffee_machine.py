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


def get_ingredients(drink_ingredients):
    """ Returns True if the ingredients are sufficient. """
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f'{item} is not enough.')
            return False
        return True
            

def process_coins():
    """ Return total of coins """
    print('Please insert coins. ')
    total = int(input('Please add quaters: ')) * 0.25
    total += int(input('Please add dimes: ')) * 0.10
    total += int(input('Please add nickels: ')) * 0.05
    total += int(input('Please add pennies: ')) * 0.01
    return total


def is_transaction(drink_cost, coins):
    """ If process coins is more than drink cost, return true. """
    if coins >= drink_cost:
        change = coins - drink_cost
        global profit   
        profit += drink_cost
        print(f'Your change is {round(change, 2)}')
        return True
    else:
        print('There is not enough money.')
        return False


def make_drink(choice, order_ingredients):
    """ Deduct the ingredients from resources. """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Enjoy your {drink} ☕️ ')


profit = 0
flag = True
while flag:
    choice = input('What would you like to drink?: Espresso/Latte/Cappuccino: ')
    if choice == 'off':
        flag = False
    elif choice == 'report':
        for item in resources:
            print(f'{item}: {resources[item]}')
            print(f'Profit: {profit}')
    else:
        drink = choice
        choice = MENU[choice]
        if get_ingredients(choice['ingredients']):
            coins = process_coins()
            if is_transaction(choice['cost'], coins):
                make_drink(choice, choice['ingredients'])
