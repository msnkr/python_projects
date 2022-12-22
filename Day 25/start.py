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
# print(data['temp'])

# Data Frame
# data_dict = data.to_dict()
# print(data_dict)

# Series
# temp_list = data['temp'].to_list()
# print(temp_list)

temp_list = data['temp'].to_list()
# Pandas class mean returns average of data. It does len and sum foir you already
# print(data['temp'].mean())

# Returns highest number in the series
print(data['temp'].max())