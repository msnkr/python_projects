from turtle import Turtle, Screen
import time
from day_20_snake import Snake
from day_20_food import Food
from day_20_scoreboard import Score


screen = Screen()
screen.title('My snake game')
screen.bgcolor('black')
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        score.add_score()
        snake.extend_segments()
        food.refresh()

    if snake.head.xcor() > 420 or snake.head.xcor() < -420 or snake.head.ycor() > 460 or snake.head.ycor() < -440:
        score.game_over()
        game_is_on = False
        
    for segment in snake.segments:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()