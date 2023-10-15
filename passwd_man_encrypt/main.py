# Password manager


# Store passwords and usernames
# Create passwords with usernames
# Encrypt all stored data

# Ask user if they'd like to create  or add a password
# if they want to create a password, add the username and ask the parameters of the password
# If they want to add a password, get the username and password

import json


def write_files(user, passwd):
    name_pass_dict = {}
    name_pass_dict[user] = passwd


def add_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    write_files(username, password)


def main():
    print("Hello User. Would you like to add a password or create a password? /n")
    print("1. Add a username and password: ")
    print("2. Create a password: ")
    print("3. Create a file: ")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_user()

if __name__ == "__main__":
    main()
