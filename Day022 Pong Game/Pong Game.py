import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

r_paddle=Paddle((380,0))
l_paddle=Paddle((-380,0))
ball=Ball()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(fun=r_paddle.up, key='Up')
screen.onkey(fun=r_paddle.down, key='Down')
screen.onkey(fun=l_paddle.up, key='w')
screen.onkey(fun=l_paddle.down, key='s')

game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision to wall -- collision with upper or lower boundary
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    # detect collision with paddles and bounce back
    if ball.distance(r_paddle)<50 and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-340:
        ball.bounce_x()

    # detect ball when it miss right paddle
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()