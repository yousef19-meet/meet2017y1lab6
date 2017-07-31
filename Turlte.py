import turtle

UP_ARROW="Up"

LEFT_ARROW="Left"

DOWN_ARROW="Down"

RIGHT_ARROW="Right"

SPACEBAR="space"

UP=0
DOWN=1
LEFT=2
RIGHT=3
direction=UP

def up ():
    print("you pressed up!")
    global direction
    direction=UP
    print(direction)
    
def down ():
    print("you pressed down!")
    direction=DOWN
    print(direction)
    
def right ():
    print("you pressed right!")
    direction=RIGHT
    print(direction)
    
def left ():
    print("you pressed left!")
    direction=LEFT
    print(direction)
    
turtle.mainloop()

