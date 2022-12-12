logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
import os
print(logo)

# Create a function
def calculate(bidders):
# If loop to loop through values in dictionary
    highest_bid = 0
    bidder_name = ''
    for value in bidders:
        # Find highest value and name
        if bidders[value] > highest_bid:
            highest_bid = bidders[value]
            bidder_name = value
    print(bidder_name, highest_bid)


# Create a while loop
should_contine = True
while should_contine:
    # Get input
    bidders = {}
    name = input('Name: ')
    bid = int(input('Bid: $'))

    # Add input to dictionary
    bidders[name] = bid
    play_again = input('Bid again?: ')
    if play_again == 'n':
        should_contine = False
        calculate(bidders)


      