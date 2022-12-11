print('Welcome to band name generator')
city = input('Whats the name of the city you grew up in? \n')
pet_name = input('What is the name of your pet? \n')

v = city
city = pet_name
pet_name = v

print(f'Your bands name is: {city} {pet_name}')
