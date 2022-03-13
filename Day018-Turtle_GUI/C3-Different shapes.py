# triangle square pentagon hexagon heptagon octagon nonagon decagon

from turtle import Turtle,Screen

screen=Screen()
my_turtle=Turtle()
def shape(side_num):
    for i in range(side_num):
        my_turtle.forward(100)
        my_turtle.left(360/side_num)

ls=['blue','pink','green','black','yellow','grey','midnight blue','dark magenta']
screen.bgcolor('alice blue')
my_turtle.pensize(3)
for sides in range(3,11):
    my_turtle.color(ls[sides-3])
    shape(sides)

screen.exitonclick()