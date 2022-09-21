# from turtle import Turtle, Screen
# from tkinter import *

# timmy = Turtle()
# my_screen = Screen()

# # my_screen.exitonclick()

# timmy.shape('turtle')
# timmy.color('red')
# timmy.pencolor('blue')
# timmy.speed(1)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electricity', 'Water', 'Fire'])
table.border = False

print(table)