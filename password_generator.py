############# Password Generator ####################
import random

characters = list(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~")


random_pass = ""
get_digits = int(input("How many: "))
for letter in range(get_digits):
    random_letter = random.choice(characters)
    random_pass += random_letter


print(random_pass)
