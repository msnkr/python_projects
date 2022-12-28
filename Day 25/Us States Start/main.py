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
is_correct = 0
guessed_states = []

while is_correct != 50:
    answer = screen.textinput(title='Guess the States', prompt=f'Name another State: ({is_correct}/50)').title()
    # 1. Find answer in row.
    states = data[data['state'] == answer]
    if answer == 'Exit':
        to_guess = []
        for row in data.state:
            if row not in guessed_states:
                to_guess.append(row)

        df = pandas.DataFrame(to_guess)
        df.to_csv('./Day 25/Us States Start/to_guess.csv')
        break
    
    for row in data.state:
        if row == answer:
            # 3. Create new turtle object to write data to map
            turtle = Turtle()
            turtle.speed(1)
            turtle.penup()
            # 4. Turtle goto location on map
            turtle.goto(float(states.x), float(states.y))
            turtle.write(f'{answer}', align='center', font=('Arial', 10, 'normal'))
            is_correct += 1
            turtle.hideturtle()
            guessed_states.append(states.state.item())

