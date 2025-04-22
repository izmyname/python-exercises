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
        self.top_score()
        self.create_scoreboard()

    def update_score(self):
        self.score += 1
        self.create_scoreboard()

    def top_score(self):
        with open("./high_score.txt", "r") as get_last_score:
            scores_list = get_last_score.readlines()
            self.high_score = int(scores_list[-1].strip())
        
        
    def create_scoreboard(self):
        self.clear()
        self.write(arg = f"Current score: {self.score} / Highest score: {self.high_score}", align = "center", font = FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("./high_score.txt", "a") as save_last_score:
                save_last_score.write(f"{self.score}\n")
            self.high_score = self.score 
            
        self.score = 0
        self.create_scoreboard()
