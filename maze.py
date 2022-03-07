def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    if front_is_clear():
        move()
    else:
        turn_left()
        move()
        turn_left()

    
while not at_goal():
    if not wall_on_right():
        turn_right()
    if wall_in_front():
        turn_left()
    else:
        move()
    
         