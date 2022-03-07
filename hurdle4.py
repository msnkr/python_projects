def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()
    turn_right()
    
while not at_goal():
    if right_is_clear():
        jump()
    if wall_in_front():
        turn_left()
    else:
        move()