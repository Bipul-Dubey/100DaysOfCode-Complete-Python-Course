from turtle import Turtle,Screen


screen=Screen()
my_turtle=Turtle()

my_turtle.shape("turtle")
my_turtle.color("blue")
my_turtle.pensize(2)
my_turtle.pencolor('red')

move=0
while move<4:
    my_turtle.forward(200)
    my_turtle.left(90)
    move+=1

screen.exitonclick()