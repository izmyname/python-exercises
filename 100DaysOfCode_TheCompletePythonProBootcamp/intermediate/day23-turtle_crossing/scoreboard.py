from turtle import Turtle

FONT = ("Fira Code Nerd Mono", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.goto( -270, 260)
        self.level = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", move=False, align='left', font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=FONT)
