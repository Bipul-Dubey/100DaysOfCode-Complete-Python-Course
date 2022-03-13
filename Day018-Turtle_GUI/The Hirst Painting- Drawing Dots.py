colors_list=[(253, 251, 248), (250, 228, 12), (198, 11, 36), (246, 234, 238), (207, 13, 11), (233, 228, 5),
        (195, 67, 21), (239, 147, 30), (45, 210, 59), (30, 91, 187), (34, 32, 153), (17, 25, 54), (245, 38, 143),
        (68, 10, 52), (224, 249, 240), (61, 205, 231), (14, 203, 220), (247, 43, 12), (64, 25, 11), (223, 20, 102)
        ]

import turtle
import random
my_turtle=turtle.Turtle()
screen=turtle.Screen()
turtle.colormode(255)
my_turtle.speed('fastest')  # speed control
my_turtle.ht()   # hide the turtle
my_turtle.penup()       # penup so no line is printing
my_turtle.setheading(220)       # set to location
my_turtle.forward(300)
my_turtle.setheading(0)
no_of_dots=100
for dot in range(1,no_of_dots+1):
        my_turtle.dot(20,random.choice(colors_list))            # dot creation of 20 size of random color
        my_turtle.forward(50)
        if dot%10==0:
            my_turtle.left(90)
            my_turtle.forward(50)
            my_turtle.left(90)
            my_turtle.forward(500)
            my_turtle.left(180)


screen.exitonclick()
