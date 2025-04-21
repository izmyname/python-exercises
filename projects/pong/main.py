from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from score import Scoreboard

screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle(-460)
r_paddle = Paddle(460)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")



game_is_on = True

while game_is_on:
    sleep(ball.speed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.bounce_y()
    
    if (ball.distance(l_paddle) < 50 and ball.xcor() < -420) or (ball.distance(r_paddle) < 50 and ball.xcor() > 420):
        ball.bounce_x()
    
    if ball.xcor() < -440:
        score.update_score_r()
        ball.reset()
    elif ball.xcor() > 440:
        score.update_score_l()
        ball.reset()
    
screen.exitonclick()