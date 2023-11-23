import random


def get_data():
    with open(r"C:\Users\Digital\Documents\GitHub\python_projects\tarot_reader\tarot.txt")as file:
        return random.choice(file.readlines())


turns = 3
while turns != 0:
    answer = input("Do you want to draw a card?: Y/N \n")
    if answer == 'y':
        print(get_data())

        turns -= 1
else:
    print("Goodbye")
    quit()
