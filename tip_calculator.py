# TOTAL BILL
bill = float(input("What is the amount on the bill?: $"))
# TOTAL BILL X 10, 12, 15
tip = int(input('How much tip would you like to leave?: 10, 12 or 15% '))
# BILL / 100, REMAINDER BILL X 100
percentage = (tip / 100) * bill + bill
# SPLIT THE BILL WITH 2 DECIMAL PLACES
split = int(input('How many people should the bill be split by?: '))
split2 = percentage / split

print(f'Every person should pay ${round(split2, 2)}')
