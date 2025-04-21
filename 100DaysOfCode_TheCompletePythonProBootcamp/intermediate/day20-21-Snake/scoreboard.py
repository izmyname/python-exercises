from turtle import Turtle

ALIGN = 'center'
FONT = ('Fira Code Nerd Font Mono', 14, 'normal')

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score()
        self.pu()
        self.color('white')
        self.ht()
        self.update_scoreboard()
        
    def score_increase(self):
        self.score += 1
        self.update_scoreboard()

    def high_score(self):
        with open("data.txt", "r") as high_score:
            self.high_score = int(high_score.read())
        
        
    def update_scoreboard(self):
        self.goto(0, 270)
        self.clear()
        self.write(arg=f"Current score: {self.score}/ The highest score: {self.high_score}", move= False, align = ALIGN, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("data.txt","w") as score:
            score.write(f"{self.high_score}")
        