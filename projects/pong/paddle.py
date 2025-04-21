from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.pu()
        self.pos_x = x
        self.goto(x, 0)
        
        
    def move_up(self):
        if self.ycor() < 240:
            self.goto(self.pos_x, self.ycor() + 20)
            
    def move_down(self):
        if self.ycor() >  - 240:
            self.goto(self.pos_x, self.ycor() - 20)
            