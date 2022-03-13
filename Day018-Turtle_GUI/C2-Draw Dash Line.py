from turtle import Turtle,Screen

screen=Screen()
my_turtle=Turtle()

for i in range(1,10):
    my_turtle.forward(20)
    my_turtle.penup()
    my_turtle.forward(20)
    my_turtle.pendown()


screen.exitonclick()