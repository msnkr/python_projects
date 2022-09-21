from turtle import Turtle, Screen
from tkinter import *

timmy = Turtle()
my_screen = Screen()

# my_screen.exitonclick()

timmy.shape('turtle')
timmy.color('red')
timmy.pencolor('blue')
timmy.speed(1)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)

my_screen.exitonclick()