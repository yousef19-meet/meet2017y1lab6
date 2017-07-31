import turtle

def up ():
    print("you pressed up!")
    global direction
    direction=UP
    print(direction)
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x,y+10)
    print(turtle.pos())
    
def down ():
    print("you pressed down!")
    direction=DOWN
    print(direction)
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x,y-10)
    print(turtle.pos())

    
def right ():
    print("you pressed right!")
    direction=RIGHT
    print(direction)
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x+10,y)
    print(turtle.pos())

    
def left ():
    print("you pressed left!")
    direction=LEFT
    print(direction)
    old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x-10,y)
    print(turtle.pos())

    
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

turtle.onkeypress(up,UP_ARROW)

turtle.onkeypress(down,DOWN_ARROW)

turtle.onkeypress(left,LEFT_ARROW)
    
turtle.onkeypress(right,RIGHT_ARROW)

turtle.listen()


    
turtle.mainloop()

