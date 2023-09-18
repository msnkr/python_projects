# from smtplib import SMTP
# from os import environ
# import random
# import datetime as dt


# now = dt.datetime.now()
# print(now.isoweekday())


# quote_list = []

# with open(r"C:\Users\mikyl\Documents\Git\python_projects\Day 32\quotes.txt", "r")as file:
#     for file_content in file.readlines():
#         quote_list.append(file_content)

# print(random.choice(quote_list))

# user = environ["email_user"]
# passwd = environ["email_pass"]


# server = SMTP("smtp.gmail.com", 587)
# server.starttls()

# server.login(user, passwd)
# server.sendmail(
#     user, user, f"Subject:This is a test\n\n {random.choice(quote_list)} ")
# server.quit()


# Get random quote from quotes.txt
# If datetime is the current day, get a random quote
# Email random quote


# random_quotes = []
# now_date = dt.datetime.now()
# user_email = environ["email_user"]
# user_pass = environ["email_pass"]


# if now_date.isoweekday() == 7:
#     with open(r"C:\Users\mikyl\Documents\Git\python_projects\Day 32\quotes.txt")as quote:
#         all_quotes = quote.readlines()
#         random_quote = random.choice(all_quotes)

#     with SMTP("smtp.gmail.com", 587)as server:
#         server.starttls()

#         server.login(user_email, user_pass)
#         server.sendmail(user_email, user_email,
#                         f"Subject:Quote of the day \n\n {random_quote}")


import pandas as pd

# data = [10, 20, 30, 40, 50, 60]
# pdata = pd.Series(data, index=["A", "B", "C", "D", "E", "F"])

# label_exists = "A" in pdata
# s = pdata + 10

# print(s.mean())


# pandas_dict = {
#     "names": ["Mike", "John", "Fiona"],
#     "age": [25, 30, 19],
# }

# df = pd.DataFrame(pandas_dict)

# df["city"] = ["new york", "chigaco", "Nebraska"]

# young_people = df[df["age"] < 30]
# summary_stats = df.describe()

# print(summary_stats)
