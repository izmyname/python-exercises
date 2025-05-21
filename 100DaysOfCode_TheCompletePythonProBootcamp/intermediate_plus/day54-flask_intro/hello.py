from flask import Flask
import random

print(random.__name__)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ =="__main__":
    app.run()

# def decoration(func):
#     def wrapper(*args):
#         print("test")
#         print("something else")
#         func(*args)
#         func(*args)
#     return wrapper


# @decoration
# def kitten(*args):
#     for arg in args:
#         print(arg)
        
# mylist = [1,2,3,4,5]

# kitten(mylist)