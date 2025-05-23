from flask import Flask, render_template

mysite = Flask(__name__)

@mysite.route("/")
def greet():
    return render_template("./index.html")

if __name__ == "__main__":
    mysite.run(debug=True)