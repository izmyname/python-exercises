from flask import Flask
import random

random_number = random.randint(0, 9)

higherlower = Flask(__name__)

@higherlower.route("/")
def guess_intro():
    return "<h1>Guess a number between 0 and 9</h1>"\
        "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcm93eHJraTRmcWw5OTRpYjJveXd2ZzR1dHNleG9udXdlN2R5cGlubyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oJZXlVZgxbEvUCWqAO/giphy.gif'/>"
        


@higherlower.route("/<int:number>")
def guess(number):
    if number == random_number:
        return "<h1 style='color: green'>Correct!</h1>"\
            "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExczFkdmx5aWRjdWh5ZHh6dmZ3OWVpNHpqbjcxaHh6YjdxdmtpeTdlZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/F3LvCOpX7vUbiTi6nN/giphy.gif'/>"
    if number < random_number:
        return "<h1 style='color: red'>Too low!</h1>"\
            "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmt0OHB6dWl2cHA5aW8wZDF5aHp4MDNreTZsMzZmY3g4ZDR1bWVociZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WrZNidKWu8Uw0/giphy.gif' />"
    if number > random_number:
        return "<h1 style='color: orange'>too high!</h1>"\
            "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTU1bHppaGFtNGFmZDZzbWp1YXRuNnB6ajJmOXozdjRrc29ucmphYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1OHK6AqIxiOA0/giphy.gif'/>"


if __name__ == "__main__":
    higherlower.run(debug=True)