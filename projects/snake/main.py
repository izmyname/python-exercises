from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_over = False

while not game_over:
    sleep(0.1)
    screen.update()
    snake.snake_move()

    if snake.snake_head.distance(food) < 20:
        food.random_spawn()
        snake.extend_snake()
        score.update_score()

    if snake.snake_head.xcor() > 390 or snake.snake_head.xcor() < - 390 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        game_over = True
        score.game_over()
        
    for segment in snake.snake_segments[1::]:
        if snake.snake_head.distance(segment) < 10:
            game_over = True
            score.game_over()

screen.exitonclick()