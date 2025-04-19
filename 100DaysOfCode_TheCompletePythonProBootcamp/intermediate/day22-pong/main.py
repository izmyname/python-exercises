from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle((-350,0))
evil_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(paddle.move_up, "w")
screen.onkey(paddle.move_down, "s")
screen.onkey(evil_paddle.move_up, "Up")
screen.onkey(evil_paddle.move_down, "Down")

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce()
        
    if (ball.distance(evil_paddle) < 50 and ball.xcor() > 320) or (ball.distance(paddle) < 50 and ball.xcor() < - 320):
        ball.paddle_bounce()
    
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.paddle_score_increase()
        
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.evil_score_increase()

screen.exitonclick()