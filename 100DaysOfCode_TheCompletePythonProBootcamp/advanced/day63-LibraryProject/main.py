from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250) ,unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.id))
    all_books = result.scalars().all()
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_title = request.form["name"]
        book_author = request.form["author"]
        book_rating = request.form["rating"]
        book=Book(title=book_title, author=book_author, rating=book_rating)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")    
    
@app.route("/edit/<int:number>", methods=["GET", "POST"])
def edit(number):
    book_to_update = db.get_or_404(Book, number)  
    if request.method == "POST":
        book_to_update.rating = request.form["rating"]
        db.session.commit() 
        return redirect(url_for("home"))
        
    return render_template("edit.html", book=book_to_update)
    
@app.route("/<int:num>")
def delete(num):
    book_to_delete = db.get_or_404(Book, num)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
