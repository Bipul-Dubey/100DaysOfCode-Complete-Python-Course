import random
import turtle
from turtle import Turtle,Screen

screen=Screen()
my_turtle=Turtle()
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colors=(r,g,b)
    return colors

def draw_spirograph(size_gap):
    for i in range(360//size_gap):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        curr_head=my_turtle.heading()
        my_turtle.setheading(curr_head+size_gap)

my_turtle.speed('fastest')
draw_spirograph(5)

screen.exitonclick()