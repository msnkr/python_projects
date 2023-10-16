# Password manager


# Store passwords and usernames
# Create passwords with usernames
# Encrypt all stored data

# Ask user if they'd like to create  or add a password
# if they want to create a password, add the username and ask the parameters of the password
# If they want to add a password, get the username and password

import json
import random

alphabet = [chr(letter) for letter in range(65, 91)] + [chr(letter) for letter in range(97, 123)]
numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_characters_list = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", "|", ";", ":", "'", "\"", "<", ">", ",", ".", "?", "/", "`", "~", "^", "\\", "(", ")", "[", "]", "{", "}", "<", ">"]

def delete_userpass():
    new_list = {}

    with open("./secrets.json", "r")as file:
        json_data = json.load(file)

    
    for index, username in enumerate(json_data):
        print("{}.{} ".format(index, username))

    to_delete = input("Which one do you want to delete?: ")



def view_usernames_passwords():
    with open("./secrets.json", "r")as file:
        json_data = json.load(file)

    for userpass in json_data:
        print(f"{userpass}: {json_data[userpass]}")


def random_passord(number, the_list):
    randomized_items = ""
    for _ in range(number):
        randomized_items += random.choice(the_list)

    return randomized_items


def create_password():
    letters = int(input("How many letters do you want to add? "))
    letters = random_passord(letters, alphabet)
    numbers = int(input("How many numbers?: "))
    numbers = random_passord(numbers, numbers_list)
    special_characters = int(input("How many special characters?: "))
    special_characters = random_passord(special_characters, special_characters_list)

    your_password = "{}{}{}".format(letters, numbers, special_characters)
    password_list = list(your_password)
    random.shuffle(password_list)
    your_new_password = "".join(password_list)
    print(f"Your password is: {your_new_password}")
    choice = input("Do you want to save it and add a username?: y/n ")

    if choice == "y":
        username = input("What username do you want to add?: ")
        write_files(username, your_new_password)
        main()


def create_file(user_dict):
    with open("./secrets.json", "w")as file:
        json.dump(user_dict, file)
    print("File created successfully")


def write_files(user, passwd):
    user_dict = {}
    user_dict[user] = passwd

    try:
        with open("./secrets.json", "r")as file:
            data = json.load(file)

            data[user] = passwd

        with open("./secrets.json", "w")as file:
            json.dump(data, file)

        print("The file has been written \n")
    except FileNotFoundError:
     create_file(user_dict)


def add_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    write_files(username, password)
    main()


def main():
    print("Hello User. Would you like to add a password or create a password? \n")
    print("1. Add a username and password: ")
    print("2. Create a password: ")
    print("3. View username and passwords: ")
    print("4. Delete a username and passwords: ")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_user()

    elif choice == "2":
        create_password()        

    elif choice == "3":
        view_usernames_passwords()

    else:
        delete_userpass()
    main()


if __name__ == "__main__":
    main()
