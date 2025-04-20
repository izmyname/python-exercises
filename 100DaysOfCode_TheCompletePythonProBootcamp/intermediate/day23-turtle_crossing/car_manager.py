from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
        
    def new_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        car.pu()
        car.goto(320, random.randint(-260, 260))
        self.cars.append(car)
        
    def move(self):
        for car in self.cars[::5]:
            car.bk(self.move_speed)
        
    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT