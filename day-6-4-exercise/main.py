'''Hurdle4 --> https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear() and (not right_is_clear()):
        move()
    else:
        if right_is_clear():
            turn_right()
            move()
            
        else:    
            turn_left()