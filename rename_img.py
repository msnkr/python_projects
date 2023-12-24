import os
import random


alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)] + \
    [chr(i) for i in range(ord('A'), ord('Z') + 1)]


def change_name():
    count = 0
    for x in os.listdir():
        if ".png" in x:
            os.rename(x, get_random())
            count += 1

    print("Renamed {} items".format(count))
    quit_pro = input("Press enter to quit: ")
    if quit_pro == " ":
        quit()


def get_random():
    random_num = random.randint(6, 20)

    letters = ""
    for _ in range(random_num):
        letters += random.choice(alphabet)

    return "{}.png".format(letters)


os.chdir(os.getcwd())
change_name()
