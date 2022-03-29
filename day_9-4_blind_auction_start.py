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

bid_again = True
while bid_again:
    name = input('What is your name? ')
    bid = int(input('What is your bid? $'))

    bidders[name] = bid

    play_again = input('Would you like to bid again? Y/N \n')
    if play_again == 'n':
        bid_again = False
        
        highest_bid = 0
        winner = ''
        for bidder in bidders:
            bid_amount = bidders[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder
        print(f'The winner is {winner} with the bid of {highest_bid}')        
    else:
        os.system('clear')

            

        
        