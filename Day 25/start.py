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

# data = pandas.read_csv('./Day 25/weather_data.csv')
# print(data['temp'])

# Data Frame
# data_dict = data.to_dict()
# print(data_dict)

# Series
# temp_list = data['temp'].to_list()
# print(temp_list)

# temp_list = data['temp'].to_list()
# Pandas class mean returns average of data. It does len and sum foir you already
# print(data['temp'].mean())

# Returns highest number in the series
# print(data['temp'].max())

# Columns
# print(data['condition'])
# print(data.condition)

# Get data in row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday.temp)
# print(monday.temp * 1.8 + 32)

# Create a dataframe from scratch
# data_dict = {
#     'students': ['Lara','Kashia', 'Mikyle' ],
#     'Score': [88, 87, 5]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv('./Day 25/new_data.csv')

# print(data)

# Squirel data
data = pandas.read_csv('./Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_color = data['Primary Fur Color']
fur_colors = ['Gray', 'Cinnamon', 'Black']
fur_count = []

# color_list = []
# count_list = []
# def check_fur_colors(item):
#     '''
#     Check fur colors. If color == True, then append count to the count list.
#     '''
#     color_list.append(item)
#     color = fur_color == item
#     count = 0
#     for x in color:
#         if x == True:
#             count += 1
#     count_list.append(count)

# for color in fur_colors:
#     check_fur_colors(color)

# data_dict = {
#     'Colors': color_list,
#     'Count': count_list
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('./Day 25/my_squirrel_data.csv')


for color in fur_colors:
    item = fur_color == color
    fur_count.append(item.values.sum())

fur_dict = {
    'Colors': fur_colors,
    'Count': fur_count
}

data = pandas.DataFrame(fur_dict)
data.to_csv('./Day 25/my_squirrel_data.csv')