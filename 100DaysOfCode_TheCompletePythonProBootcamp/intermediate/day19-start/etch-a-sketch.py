from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()

def forwards():
    pen.fd(10)

def backwards():
    pen.bk(10)

def counter_clockwise():
    pen.right(10)

def clockwise():
    pen.left(10)

def clearscreen():
    screen.reset()

screen.onkey(key = 'w', fun = forwards)
screen.onkey(key = 's', fun = backwards)
screen.onkey(key = 'a', fun = counter_clockwise)
screen.onkey(key = 'd', fun = clockwise)
screen.onkey(key = 'c', fun = clearscreen)

screen.listen()
screen.exitonclick()