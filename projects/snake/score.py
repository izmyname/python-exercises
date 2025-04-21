from turtle import Turtle

FONT = ("Fira Code Nerd Mono", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.goto(0, 260)
        self.ht()
        self.score = 0
        self.create_scoreboard()

    def update_score(self):
        self.score += 1
        self.clear()
        self.create_scoreboard()
        
    def create_scoreboard(self):
        self.write(arg = f"Score: {self.score}", align = "center", font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg = f"GAME OVER", align = "center", font = FONT)