from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        
    def move(self):
        self.fd(MOVE_DISTANCE)
        
    def player_return(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
