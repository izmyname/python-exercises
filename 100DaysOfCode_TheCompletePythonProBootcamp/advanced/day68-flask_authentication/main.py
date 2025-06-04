from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# configure flask-login
login_manager = LoginManager()
login_manager.init_app(app)

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
    
    


with app.app_context():
    db.create_all()
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        crypt= generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8)
        user_email = request.form.get("email")
        check_user = db.session.execute(db.select(User).where(User.email == user_email)).scalar()
        if check_user:
            flash("You've already signed up with this email. Try to login, instead")
            return redirect(url_for("login"))
        
        new_user=User(
            email=user_email,
            password=crypt,
            name=request.form.get("name")
            )
        session["name"]=new_user.name
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("secrets"))
    return render_template("register.html")


@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        user_email=request.form.get("email")
        user_password=request.form.get("password")
        user = db.session.execute(db.select(User).where(User.email == user_email)).scalar()
        try:
            check_password = check_password_hash(user.password, user_password)
        except AttributeError:
            flash("A user with this email doesn't exist")
            return redirect(url_for("login"))
        if not check_password:
            flash("Incorrect password")
            return redirect(url_for("login"))
        if user.email and check_password:
            login_user(user)
            return redirect(url_for("secrets"))
        
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", username=session["name"])


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory("./static/files", "cheat_sheet.pdf", as_attachment=False)


if __name__ == "__main__":
    app.run(debug=True)
