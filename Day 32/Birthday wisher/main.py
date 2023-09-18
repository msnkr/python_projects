##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)


import datetime as dt
import random
from smtplib import SMTP
import os
import pandas as pd


USER_EMAIL = os.environ["email_user"]
USER_PASS = os.environ["email_pass"]


now = dt.datetime.now()
today = now.day
month = now.month

csv_location = r"C:\Users\Digital\Documents\GitHub\python_projects\Day 32\Birthday wisher\birthdays.csv"
df = pd.read_csv(csv_location)


def get_random_letter(name):
    random_number = random.randint(1, 3)
    with open(fr"C:\Users\Digital\Documents\GitHub\python_projects\Day 32\Birthday wisher\letter_templates\letter_{random_number}.txt", "r+")as letter:
        letter_contents = letter.read()
        letter_and_name = letter_contents.replace("[NAME]", name)
        return letter_and_name


for column_name, column_item in df.iterrows():
    birthday_day = column_item["day"]
    birthday_month = column_item["month"]

    if birthday_day == today and birthday_month == month:
        name = column_item["name"]

        letter = get_random_letter(name)
