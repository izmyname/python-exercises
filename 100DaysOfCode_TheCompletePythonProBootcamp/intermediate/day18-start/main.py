from turtle import Turtle, Screen
import heroes as lol
import villains
import turtle
import random

leo = Turtle("turtle")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return (r, g, b)


# # for x in range(4):
    
# #     leo.forward(100)
# #     leo.left(90)


# # y = 0

# # while y < 8:
# #     leo.right(45)
# #     leo.forward(150)
# #     y += 1


# # def dashed_line():
# #     for x in range(20):
        
# #         leo.forward(10)
# #         leo.penup()
# #         leo.fd(5)
# #         leo.pd()
        

# # for i in range(4):
# #     dashed_line()
# #     leo.left(90)


# # random walk

# leo.speed(10)
# leo.pensize(10)

# direction = ( 90, -90, 0, 180, )

# def random_walk():
    
#     leo.color(random_color())
#     leo.setheading(random.choice(direction))
#     leo.fd(30)


# x = 0

# while x < 500:
#     random_walk()
#     x += 1


# # draw shapes

# # def draw_shape(num_of_corners):
    
# #     degree = 360/num_of_corners
    
# #     for x in range(num_of_corners):
        
# #         leo.fd(100)
# #         leo.right(degree)
        
    
# # for c in range (3,11):
        
# #     leo.color(random_color())
# #     draw_shape(c)



# My spirograph


# for i in range(200):
    
#     leo.color(random_color())
#     leo.circle(100)
#     leo.left(5)
    
#     # I should've use setheading() and heading(), but that works too


# Correct spirograph

leo.speed("fastest")

def spirograph(degree):
    
    for d in range(int(360/degree)):
        
        leo.color(random_color())
        leo.circle(100)
        leo.setheading(leo.heading() + degree)
        

spirograph(10)


the_screen = Screen()
the_screen.exitonclick()

# # print(f"{lol.gen()} versus {villains.gen()}")