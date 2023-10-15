# Password manager


# Store passwords and usernames
# Create passwords with usernames
# Encrypt all stored data

# Ask user if they'd like to create  or add a password
# if they want to create a password, add the username and ask the parameters of the password
# If they want to add a password, get the username and password
import random

def create_file():
    with open("./secret.txt", "w")as file:
        file.write("Your keys will be saved here")
    print("File saved")
    main()


def search_file():
    try:
        with open("./secret.txt", "r")as file:
            file.readlines()
    except FileNotFoundError as err:
        create_file()

def add_user():
    search_file()
    username = input("Enter your username: ")
    password = input("Enter your password: ")


def main():
    print("Hello User. Would you like to add a password or create a password?: ")
    print("1. Add a username and password: ")
    print("2. Create a username and password: ")
    print("3. Create a file: ")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_user()
    elif choice == "3":
        create_file()

if __name__ == "__main__":
    main()
