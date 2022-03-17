import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.up,'Up')

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect turtle collision with cars
    for car in car_manager.all_cars:
        if car.distance(player)<25:
            game_on=False
            scoreboard.game_over()

    # detect car on other side of wall
    if player.is_at_finish_line():
        player.start_again()
        car_manager.level_up()
        scoreboard.increase_level()
        # scoreboard.update_scoreboard()




screen.exitonclick()