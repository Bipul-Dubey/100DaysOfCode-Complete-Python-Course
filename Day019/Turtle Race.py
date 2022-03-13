import random
from turtle import Turtle, Screen

screen = Screen()

screen.setup(600,600)    # setting width,height
bet_turtle=screen.textinput(title='Make your bet',prompt="which turtle win: ")  # taking input from user
colors=['red','orange','yellow','green','blue','purple',]
all_turtle=[]

is_race_on=False

for turtle_index in range(0,6):
    turtles=Turtle(shape='turtle')
    turtles.penup()
    turtles.color(colors[turtle_index])
    turtles.goto(x=-290, y=130 - (turtle_index * 50))
    all_turtle.append(turtles)

if bet_turtle:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>265:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==bet_turtle:
                print(f"You've Won!! The {winning_color} turtle is winner!!")
            else:
                print(f"You've lost!! The {winning_color} turtle is winner!!")
        rand_distance=random.randint(0,11)
        turtle.forward(rand_distance)


screen.exitonclick()