def turn_right():
    turn_left()
    turn_left()
    turn_left()

def moving():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 6
while number_of_hurdles > 0:
    moving()
    # need to add another line or it will be an infinity loop
    number_of_hurdles -= 1
