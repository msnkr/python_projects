import requests

# response = requests.get("http://api.open-notify.org/iss-now.json")

# if response.ok:
#     data = response.json()
#     iss_position = data["iss_position"]
#     position = {data: iss_position[data] for data in iss_position}

#     print(position["longitude"])
#     print(position["latitude"])

MY_LAT = -26.204103
MY_LNG = 28.047304
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}


def split_data(data):
    return data.split("T")[1].split(":")[0]


response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)

if response.ok:
    data = response.json()["results"]
    sunrise = data["sunrise"]
    sunset = data["sunset"]

    sunrise_time = split_data(sunrise)
    sunset_time = split_data(sunset)


    print(sunrise_time)
