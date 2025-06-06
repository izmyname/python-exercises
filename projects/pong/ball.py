from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.pu()
        self.goto(0,0)
        self.x_cor = 10
        self.y_cor = 10
        self.speed = 0.1
        
    
    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_cor *= (-1)
        
    def bounce_x(self):
        self.x_cor *= (-1)
        self.speed *= 0.8
        
    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.speed = 0.1
        