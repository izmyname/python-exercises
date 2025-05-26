from flask import Flask, render_template,abort
import requests

blog = Flask(__name__)

blog_posts = requests.get(url="https://api.npoint.io/2e9b617862534593bb58").json()


@blog.route("/")
def my_blog():
    return render_template("index.html", blogs=blog_posts)

@blog.route("/about")
def about():
    return render_template("about.html")

@blog.route("/contact")
def contact():
    return render_template("contact.html")

@blog.route("/post/<int:number>")
def post(number):
    blog = {}
    match number:
        case 1:
            blog = blog_posts[0]
        case 2:
            blog = blog_posts[1]
        case 3:
            blog = blog_posts[2]
        case _:
            abort(404)
        
    return render_template("post.html", blog=blog)

if __name__ == "__main__":
    blog.run(debug=True)