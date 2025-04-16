from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title='I don\'t use titlebars', prompt='Which turtle will win? Choose a color:').lower()
race_is_on = False

participants = {
    "leo": "blue",
    "raph": "red",
    "mike": "orange",
    "don": "violet",
    "tim": "green",
    "tom": "black",
}

starting_line = []


y_pos = -120

for t in participants:
    y_pos += 30
    color = participants[t]

    t = Turtle(shape="turtle")
    t.color(color)
    t.pu()
    t.goto(x=-240, y=y_pos)
    starting_line.append(t)
    
    

if user_bet:
    race_is_on = True

while race_is_on:
    
    for p in starting_line:
        if p.xcor() > 210:
            win_color = p.pencolor()
            race_is_on = False
            if win_color == user_bet:
                print(f"{p.pencolor()} won! Congratulations")
            else:
                print(f"The winner is {p.pencolor()}. You lose.")
        
        random_step = random.randint(5, 20)
        p.forward(random_step)


screen.exitonclick()
