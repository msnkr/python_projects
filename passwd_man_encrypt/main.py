# Password manager


# Store passwords and usernames
# Create passwords with usernames
# Encrypt all stored data

# Ask user if they'd like to create  or add a password
# if they want to create a password, add the username and ask the parameters of the password
# If they want to add a password, get the username and password
import random


def search_file():
    pass


def generate_name():
    random_name = ""
    alphabet = [chr(letter) for letter in range(97, 123)]
    for _ in range(12):
        random_name += random.choice(alphabet)

    return random_name


def add_user():
    search_file()
    username = input("Enter your username: ")
    password = input("Enter your password: ")


def main():
    print("Hello User. Would you like to add a password or create a password?: ")
    print("1. Add a username and password: ")
    print("2. Create a username and password: ")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_user()


if __name__ == "__main__":
    main()
