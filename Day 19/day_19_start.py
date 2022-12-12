from turtle import Turtle, Screen
import random


# tim = Turtle()
# tim.speed(0)
# screen = Screen()

# screen.listen()

# def move_forwards():
#     tim.forward(50)

# def move_backwards():
#     tim.backward(50)

# def move_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)

# def move_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)



# screen.onkey(fun=move_forwards, key='w')
# screen.onkey(fun=move_backwards, key='s')
# screen.onkey(fun=move_left, key='a')
# screen.onkey(fun=move_right, key='d')
# screen.onkey(fun=tim.reset, key='c')
# screen.exitonclick()



screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'yellow', 'orange', 'green', 'blue', 'purple']
is_race_on = False
user_guess = screen.textinput(title='Place your bets', prompt='Guess which color will cross the finish line first.')
y_positions = [-300, -200, -100, -0, 100, 200]
all_turtles = []


for x in range(6):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.goto(x=-400, y=y_positions[x])
    tim.color(colors[x])
    all_turtles.append(tim)

is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        if turtle.xcor() > 420:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_guess:
                print(f'You\'ve Won! The winning turtle is {turtle.pencolor()}')
            else:
                print(f'You\'ve Lost! The winning turtle is {turtle.pencolor()}')
            is_race_on = False




screen.exitonclick()