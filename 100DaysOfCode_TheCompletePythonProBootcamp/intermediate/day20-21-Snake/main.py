from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title('Snake Game')
screen.tracer(0)


game_is_on = True


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_increase()
        
    if snake.head.xcor() > 290 or snake.head.xcor() < - 290 or snake.head.ycor() > 290 or snake.head.ycor() < - 290:
        game_is_on = False
        scoreboard.game_over()    
        
        
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
