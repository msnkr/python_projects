from turtle import Turtle, Screen
import pandas


# def get_current_coor(x, y):
#     '''
#     Get current coordinates when you click on the screen
#     '''
#     print(x, y)

# screen.onscreenclick(get_current_coor)


image = './Day 25/Us States Start/blank_states_img.gif'
csv_file = './Day 25/Us States Start/50_states.csv'
data = pandas.read_csv(csv_file)

screen = Screen()
screen.title('My US States Game')
screen.addshape(image)
turtle = Turtle(shape=image)


# 2. Create new text.
game_on = True
while game_on:
    answer = screen.textinput(title='Guess the States', prompt='Name another State: ').capitalize()
    # 1. Find answer in row.
    states = data[data['state'] == answer]
    # 3. Create new turtle object to write data to map
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.speed(4)
    # 4. Turtle goto location on map
    turtle.goto(float(states.x), float(states.y))
    turtle.write(f'{answer}', align='center', font=('Arial', 10, 'normal'))


screen.exitonclick()