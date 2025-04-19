from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.pu()
        self.goto(pos)
        
    def move_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() +20)

    def move_down(self):
        if self.ycor() > - 240:
            self.goto(self.xcor(), self.ycor() -20)
