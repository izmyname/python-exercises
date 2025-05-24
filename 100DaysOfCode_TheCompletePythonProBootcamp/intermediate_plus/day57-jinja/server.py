from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    cheezburger="I'm a string"
    date_year = datetime.now().strftime("%Y")
    return render_template("index.html", lolcat=cheezburger, year = date_year)

@app.route("/<name>")
def name_guess(name):
    
    query = {
        "name":name ,
    }
    
    genderize = "https://api.genderize.io/"
    agify = "https://api.agify.io/"
    
    age = requests.get(url=agify, params=query)
    gender = requests.get(url=genderize, params=query)
    
    name = name.title()
    gender = gender.json()["gender"]
    age = age.json()["age"]
    
    return render_template("name.html", username=name, usergender=gender, userage=age)

@app.route("/blog")
def get_blog():
    blogs = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blogs)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

