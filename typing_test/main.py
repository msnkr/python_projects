from tkinter import *
import faker


fake = faker.Faker()

def word_list():
    return " ".join([fake.word().lower() for _ in range(20)])





# Create app using tkinter
# When click start
# Show words on left, your typing on right
# Countdown timer for 30 seconds
# When 30 secodns are up, count all the correct words and compare.
# Find out how to get words per minute
