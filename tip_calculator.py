# TOTAL BILL
bill = float(input('What is the total amount?: '))
# TOTAL BILL X 10, 12, 15 
tip = input('How much tip would you like to leave?: ')
# BILL / 100, REMAINDER BILL X 100
percentage = bill / 100 
tip = percentage * 100
# SPLIT THE BILL WITH 2 DECIMAL PLACES
people = int(input('How many people?'))

split = round(tip, 2) 

print(split / people)