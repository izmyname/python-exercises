from flask import Flask, render_template
from post import Post

post = Post()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blogs=post.get_blogs())

@app.route("/blogs/<int:number>")
def post_body(number):
    return render_template("post.html", title=post.title(number), subtitle=post.subtitle(number), body=post.body(number))

if __name__ == "__main__":
    app.run(debug=True)
