from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.pu()
        self.random_spawn()
        
    def random_spawn(self):
        rand_x = random.randint(-360, 360)
        rand_y = random.randint(-260, 260)
        self.clear()
        self.goto(rand_x, rand_y)
        