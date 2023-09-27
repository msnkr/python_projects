import requests
from datetime import datetime
from smtplib import SMTP
import os
import time


# MY_EMAIL = os.environ("email_user")
# MY_PASS = os.environ("email_pass")

MY_LAT = -26.204103
MY_LNG = 28.047304


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def is_close(MY_LAT, MY_LNG, iss_latitude, iss_longitude):
    if MY_LAT == iss_latitude + 5 or MY_LAT == iss_latitude - 5 and MY_LNG == iss_longitude + 5 or MY_LNG == iss_longitude - 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

while True:
    if time_now > sunset or time_now < sunrise:
        if is_close(MY_LAT, MY_LNG, iss_latitude, iss_longitude):
            print("Email sent")
            # with SMTP("smtp.gmail.com")as server:

            #     server.starttls()
            #     server.connect(MY_EMAIL, MY_PASS)
            #     server.sendmail(
            #         MY_EMAIL, MY_EMAIL, msg="Subject: Look Up bro \n\n Look to the sky for the ISS satelite bro. ")
        else:
            print("Not here")
    else:
        print("Not time")
    time.sleep(60)


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
