from turtle import Turtle,Screen
FONT=('Courier',18, 'normal')
ALIGNMENT='Right'

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.ht()
        self.penup()
        self.goto(x=0,y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
