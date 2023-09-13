from smtplib import SMTP
from os import environ

user = environ["email_user"]
passwd = environ["email_pass"]


server = SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(user, passwd)
server.sendmail(user, user, "Subject:This is a test\n\n How are you? ")
server.quit()
