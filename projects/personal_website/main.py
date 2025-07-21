from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import smtplib
from datetime import datetime
from form import MyForm
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["APP_KEY"]
Bootstrap5(app)

@app.context_processor
def year_now():
    return {"current_year": datetime.now().strftime("%Y")}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    myform = MyForm()
    if myform.validate_on_submit():
        sender = myform.email.data
        body = myform.body.data
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=os.environ["MY_MAIL"], password=os.environ["MY_PASS"])
            connection.sendmail(from_addr=sender, to_addrs=os.environ["MY_MAIL"], msg=f"Subject:A new message from your portfolio website\n\n{body}") 
            return redirect(url_for("home"))
    return render_template("contact.html", form = myform)

if __name__ == "__main__":
    app.run(debug=True)
