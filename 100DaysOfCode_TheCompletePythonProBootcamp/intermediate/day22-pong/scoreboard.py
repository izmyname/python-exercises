from turtle import Turtle

ALIGN = 'center'
FONT = ('Fira Code Nerd Font Mono', 48, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.paddle_score = 0
        self.evil_paddle_score = 0
        self.color("white")
        self.ht()
        self.pu()
        self.goto(0, 220)
        self.update_scoreboard()
    
    def paddle_score_increase(self):
        self.paddle_score += 1
        self.update_scoreboard()
        
    def evil_score_increase(self):
        self.evil_paddle_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"{self.paddle_score} : {self.evil_paddle_score}", move= False, align = ALIGN, font=FONT)