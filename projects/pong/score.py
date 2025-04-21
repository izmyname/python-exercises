from turtle import Turtle

FONT = ("Fira Code Nerd Mono", 48, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.ht()
        self.goto(0, 220)
        self.l_score = 0
        self.r_score = 0
        self.create_score()
        
    def update_score_l(self):
        self.l_score += 1
        self.create_score()
        
    def update_score_r(self):
        self.r_score += 1
        self.create_score()
        

    def create_score(self):
        self.clear()
        self.write(arg = f"{self.l_score}:{self.r_score}", align = "center", font = FONT)
