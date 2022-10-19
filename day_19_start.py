from turtle import Turtle, Screen

tim = Turtle()
tim.speed(0)
screen = Screen()

screen.listen()

def move_forwards():
    tim.forward(50)

def move_backwards():
    tim.backward(50)

def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)



screen.onkey(fun=move_forwards, key='w')
screen.onkey(fun=move_backwards, key='s')
screen.onkey(fun=move_left, key='a')
screen.onkey(fun=move_right, key='d')
screen.onkey(fun=tim.reset, key='c')
screen.exitonclick()