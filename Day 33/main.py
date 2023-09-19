import requests

response = requests.get("http://api.open-notify.org/iss-now.json")

if response.ok:
    data = response.json()
    iss_position = data["iss_position"]
    position = {data: iss_position[data] for data in iss_position}

    print(position)
