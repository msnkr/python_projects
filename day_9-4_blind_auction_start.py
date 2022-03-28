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

bid_again = True
while bid_again:
    os.system('clear')
    bidders = []
    name = input('What is your name? ')
    bid = int(input('What is your bid? $'))
    
    current_bid = {
        'name': name,
        'bid': bid,
    }

    bidders.append(current_bid)
    play_again = input('Would you like to bid again? Y/N \n')
    if play_again == 'n':
        bid_again = False


print(bidders)
