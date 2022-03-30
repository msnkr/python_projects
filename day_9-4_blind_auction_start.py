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


bidders = {}
should_contine = True

def calculate(bidders):
    highest_bid = 0
    name_of_bidder = ''
    for value in bidders:
        if bidders[value] > highest_bid:
            highest_bid = bidders[value]
            name_of_bidder = value

    print(f'The highest bidder is {name_of_bidder} with the bid of ${highest_bid}.')     

    
while should_contine:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))
    bidders[name] = bid

    play_again = input('Would anyone else like to bid?: Y/N \n').lower()
    if play_again == 'n':
        should_contine = False
        calculate(bidders)

      