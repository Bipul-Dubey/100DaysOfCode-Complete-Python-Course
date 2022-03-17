import turtle
from turtle import Turtle
FONT=('Courier',18, 'normal')
ALIGNMENT='Right'

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open('data.txt') as data:
            self.high_score=int(data.read())
        self.color('white')
        self.ht()
        self.penup()
        self.goto(x=25,y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        game_end=turtle.Turtle()
        game_end.color('white')
        game_end.goto(0,0)
        game_end.write(f"Game Over", align='center', font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open('data.txt',mode='w') as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
