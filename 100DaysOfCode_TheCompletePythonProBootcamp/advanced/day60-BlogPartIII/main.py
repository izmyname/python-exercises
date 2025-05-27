from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

posts = requests.get("https://api.npoint.io/2e9b617862534593bb58").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    post_request= ""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        post_request = "Successfully sent your message!"
        
        with smtplib.SMTP(os.environ["SMTP"], 587) as connection:
            connection.starttls()
            connection.login(user=os.environ["MY_MAIL"], password=os.environ["MY_PASSWD"])
            connection.sendmail(from_addr=os.environ["MY_MAIL"], to_addrs=os.environ["RECEIVER"], msg=f"Subject:Blog feedback:\n\nName: {name}\nEmail: {email}\nPhone: {phone}\n Message:\n{message}")    
        
        return render_template("contact.html", post_request=post_request)
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
