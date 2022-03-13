from turtle import Turtle, Screen

screen=Screen()
my_turtle=Turtle()

def move_right():
    my_turtle.setheading(0)
    move=my_turtle.forward(20)
    return move

def move_Up():
    my_turtle.setheading(90)
    move=my_turtle.forward(20)
    return move

def move_left():
    my_turtle.setheading(180)
    move=my_turtle.forward(20)
    return move

def move_down():
    my_turtle.setheading(270)
    move=my_turtle.forward(20)
    return move



screen.listen()
screen.onkey(key='Right',fun=move_right)
screen.onkey(key='Up',fun=move_Up)
screen.onkey(key='Left',fun=move_left)
screen.onkey(key='Down',fun=move_down)


screen.exitonclick()