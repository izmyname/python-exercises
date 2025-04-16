from turtle import Turtle, Screen


mike = Turtle("turtle")
screen = Screen ()

def move_forward():
    mike.fd(100)

screen.listen()
screen.onkey(move_forward, 'space')


screen.exitonclick()