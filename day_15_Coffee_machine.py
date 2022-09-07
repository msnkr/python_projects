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


# If the resources are sufficiaent, Prompt the user for coins. Quaters == .25c, Dimes == .10c, Nickels == .5c and Pennies == .1c
    # Find a way to extract the info you need. Coins will equal 0 and every add with add to coins
    # Make a function that checks the coins

# If prompt is off then quit the program
    #While prompt doesn't equal off:
answer = ''
monies = 0
while answer != 'off':
    # Ask user what they would like
    answer = input('What would you like to order?: Espresso/Latte/Capuccino: ')
    # If prompt is report then show available resources and money
    if answer == 'report':
        for item in resources:
            print(f'{item}: {resources[item]}')


# Check if the money is suffiecient, If not return the coins and start again, if its exact then its fine, if coins are over then return change.
    # If price > coffee, return not sufficient. If price == coffee, proceed, else price - coins, return price.
# If resources are sufficient and money is suffiectn then the resources reqiured should be subtracted from the resources. 
    # Maybe add resources to a new dictionary
# When Done. The program should say enjoy your {drink}
