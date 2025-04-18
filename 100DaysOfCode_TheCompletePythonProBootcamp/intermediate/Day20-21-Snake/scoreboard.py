from turtle import Turtle

ALIGN = 'center'
FONT = ('Fira Code Nerd Font Mono', 14, 'normal')

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.color('white')
        self.ht()
        self.update_scoreboard()
        
    def score_increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}", move= False, align = ALIGN, font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game over".upper(), move= False, align = ALIGN, font=FONT)
    