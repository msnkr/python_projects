# with open('./Day 25/weather_data.csv')as f:
#     weather_data = f.readlines()
#     print(weather_data)

import csv

with open('./weather_data.csv')as data:
    weather = csv.reader(data)
    temperature_list = []
    for row in weather:
        if row[1] != 'temp':
            temperature_list.append(int(row[1]))

    
print(temperature_list)