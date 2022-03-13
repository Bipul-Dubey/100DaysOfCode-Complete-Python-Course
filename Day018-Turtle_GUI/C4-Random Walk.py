from turtle import Turtle, Screen
import random

my_turtle=Turtle()
screen=Screen()
colors=['blue','pink','green','black','yellow','grey','midnight blue','dark magenta']
directions=[0,90,180,270]


screen.bgcolor('alice blue')  # change screen background color
my_turtle.pensize(7)  # change size of pen
my_turtle.speed('fast')  # speed of pen (slowest,slow,normal,fast,fastest)
for i in range(100):
    random_color=random.choice(colors)
    random_dir=random.choice(directions)
    my_turtle.forward(30)
    my_turtle.setheading(random_dir)    # moving in given direction
    my_turtle.color(random_color)




screen.exitonclick()