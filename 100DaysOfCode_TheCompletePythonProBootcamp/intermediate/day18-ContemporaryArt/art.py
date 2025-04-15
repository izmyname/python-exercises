from turtle import Turtle, Screen
import turtle
import random
import colorgram as col


# colors = col.extract('image.jpeg', 30 )

# my_colors = []

# for c in colors:
    
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b

#     formatted_color = (r, g, b)
#     my_colors.append(formatted_color)
    
    
# my_colors.pop(0)
# my_colors.pop(0)

my_colors = [(234, 35, 109), (230, 236, 231), (237, 73, 34), (149, 27, 63), (6, 148, 94), (213, 228, 234), (230, 168, 41), (181, 158, 46), (27, 126, 193), (43, 191, 230), (85, 27, 92), (253, 223, 0), (125, 192, 75), (243, 219, 50), (181, 39, 101), (80, 179, 91), (209, 57, 32), (209, 131, 167), (151, 25, 23), (24, 187, 226), (236, 163, 193), (239, 169, 157), (162, 212, 175), (139, 211, 230), (3, 119, 56), (72, 136, 185), (179, 188, 211), (117, 6, 5)]



raf = Turtle("turtle")
turtle.colormode(255)

y_pos = -200

# set position
raf.pu()
raf.setpos(-500, y_pos)
raf.pd()


def draw_string():
    
    
    for x in range(10):
    
        rand_color = random.choice(my_colors)
        raf.dot(20, rand_color)
        raf.pu()
        raf.fd(50)   
        
        
        
for s in range (10):
    
    y_pos += 50
    
    draw_string()
    raf.setpos( -500, y_pos)   
    
raf.ht()   

the_screen = Screen()
the_screen.exitonclick()
