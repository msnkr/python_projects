# with open('./Day 25/weather_data.csv')as f:
#     weather_data = f.readlines()
#     print(weather_data)

import csv

with open('./Day 25/weather_data.csv')as data:
    weather = csv.reader(data)
    temperature_list = []
    for row in weather:
        temp_items = row[1]
        temperature_list.append(new_temp)
    print(temperature_list)