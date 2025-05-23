from flask import Flask, render_template

webpage = Flask(__name__)

@webpage.route("/")
def my_site():
    return render_template("./index.html")


if __name__ == "__main__":
    webpage.run(debug=True)