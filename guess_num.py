############# Guess the number ####################
from random import randint

tries = 10
random_num = randint(0, 100)
flag = True

while flag:
    guess = int(input("Guess the number between 0 and 100 \n"))
    print(f"You have {tries} left")
    if tries == 0:
        flag = False
    else:
        if guess == random_num:
            print("Just right")
            flag = False
        elif guess < random_num:
            print("Too low")
            tries -= 1
        else:
            print("too high")
            tries -= 1
