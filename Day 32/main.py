from smtplib import SMTP
from os import environ
import random


quote_list = []

with open(r"C:\Users\Digital\Documents\GitHub\python_projects\Day 32\quotes.txt", "r")as file:
    for file_content in file.readlines():
        quote_list.append(file_content)

print(random.choice(quote_list))

# user = environ["email_user"]
# passwd = environ["email_pass"]


# server = SMTP("smtp.gmail.com", 587)
# server.starttls()

# server.login(user, passwd)
# server.sendmail(
#     user, user, f"Subject:This is a test\n\n {random.choice(quote_list)} ")
# server.quit()
