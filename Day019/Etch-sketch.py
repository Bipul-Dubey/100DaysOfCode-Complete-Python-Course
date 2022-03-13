from turtle import Turtle, Screen

screen=Screen()
my_turtle=Turtle()

def move_forward():
    move=my_turtle.forward(20)
    return move

def move_backward():
    return my_turtle.backward(20)


def turn_left():
    return my_turtle.left(10)

def turn_right():
    return my_turtle.right(10)

def clr_screen():
    screen.reset()

screen.listen()
screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='a',fun=turn_left)
screen.onkey(key='d',fun=turn_right)
screen.onkey(key='c',fun=clr_screen)

screen.exitonclick()