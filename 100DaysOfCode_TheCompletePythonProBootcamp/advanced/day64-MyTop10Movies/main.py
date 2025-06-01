from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange, Length
import requests
import os
from dotenv import load_dotenv

load_dotenv()


# Configure Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_top_10_movies.db"
db.init_app(app)


# CREATE TABLE

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=True)
    ranking: Mapped[int] = mapped_column(nullable=True)
    review: Mapped[str] = mapped_column(nullable=True)
    img_url: Mapped[str] = mapped_column()


with app.app_context():
    db.create_all()
    

#Create WTForm for editing the movies

class MyForm(FlaskForm):
    rating = DecimalField(label='Your rating', validators=[DataRequired(message="The field is empty."), NumberRange(min=1, max=10, message="Invalid number. Only numbers from 1 to 10 are allowed.")])
    review = StringField(label='Your Review', validators=[DataRequired(message="The field is empty"), Length(max=500, message="Your review is longer than 500 symbols.")])
    submit = SubmitField("Update")
    
# Create WTForm for TMDB
class AddMovie(FlaskForm):
    movie = StringField(label='Movie Title', validators=[DataRequired(message="The field is empty")])
    submit = SubmitField("Add Movie")

#HEaders for TMDB
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.environ["API_TOKEN"]}"
    }

#Create form to return without choosing a film
class Return(FlaskForm):
    submit = SubmitField("Return to the main page")
    


@app.route("/")
def home():
    my_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    rank=0
    for movie in my_movies[::-1]:
        rank +=1
        movie.ranking = rank
        db.session.commit()
    return render_template("index.html", movies=my_movies)

@app.route("/edit", methods=["GET","POST"])
def edit():
    form = MyForm()
    movie_id = request.args.get('id')
    movie_edit = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie_edit.rating = form.rating.data
        movie_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie_edit)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    delete_movie = db.get_or_404(Movie, movie_id)
    db.session.delete(delete_movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    movie_form = AddMovie()
    return_form = Return()

    
    # Get data from TMDB
    parameters = {
        "query": movie_form.movie.data,
        "include_adult": True,
    }

    if movie_form.validate_on_submit():
        response = requests.get("https://api.themoviedb.org/3/search/movie", params=parameters, headers=headers).json()["results"]
        return render_template("select.html", movies_data = response)  
        
    if return_form.validate_on_submit():
        return redirect(url_for('home'))   
    return render_template("add.html", movie_form = movie_form, return_form = return_form)


@app.route("/select", methods=["GET", "POST"])
def select():
    
    movie_id = request.args.get('id')
    response = requests.get(f" https://api.themoviedb.org/3/movie/{movie_id}", headers=headers).json()
    title = response["title"]
    poster = f"https://image.tmdb.org/t/p/original{response['poster_path']}"
    year = response["release_date"][:4:]
    description = response["overview"]
    movie = Movie(title=title, year=year,description=description,img_url=poster)
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for('edit', id=movie.id))



if __name__ == '__main__':
    app.run(debug=True)