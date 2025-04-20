import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "space") 
screen.onkey(player.move, "Up") 

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.new_car()
    cars.move()
    screen.update()
    for n in cars.cars:
        if player.distance(n) <20:
            game_is_on = False
            score.game_over()
            
    if player.ycor() >= FINISH_LINE_Y:
        player.player_return()
        score.update_scoreboard()
        cars.increase_speed()
        
screen.exitonclick()