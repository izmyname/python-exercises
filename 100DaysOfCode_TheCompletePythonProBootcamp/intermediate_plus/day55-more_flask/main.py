from flask import Flask

myapp = Flask(__name__)

# @myapp.route("/user/<name>/<int:number>/")
# def greet(name, number):
#         return f"<h1 style='color: red'>What do you want, my dear {name}? {number} coins?</h1>"\
#         "<p style='text-align: center'>I'm just a paragraph</p>"\
#             "<h2 style='color: blue'>kekekeke</h2>"
    
# if __name__ == "__main__":
#     myapp.run(debug=True)

# def make_bold(func):
#     def wrapper():
        
        
#     return wrapper

def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def underline(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

def align_center(func):
    def wrapper():
        return f"<p style='text-align: center'>{func()}</p>"
    return wrapper

def red(func):
    def wrap():
        return f"<h2 style='color: red'>{func()}</h2>"
    return wrap

def italic(func):
    def wrap():
        return f"<i>{func()}</i>"
    return wrap

@myapp.route("/lol")
@bold
@underline
@italic
@red
@align_center
def lol():
    return "lol"


if __name__ == "__main__":
    myapp.run(debug=True)


