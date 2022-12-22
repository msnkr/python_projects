# with open('./Day 25/weather_data.csv')as f:
#     weather_data = f.readlines()
#     print(weather_data)

# import csv

# with open('./weather_data.csv')as data:
#     weather_data = csv.reader(data)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

# print(temperatures)
    
import pandas

data = pandas.read_csv('./Day 25/weather_data.csv')
print(data['temp'])
