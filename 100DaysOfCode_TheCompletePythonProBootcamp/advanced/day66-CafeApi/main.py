from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random


app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe=Cafe(
        name=request.form["name"],
        map_url=request.form["map_url"],
        img_url=request.form["img_url"],
        location=request.form["location"],
        seats=request.form["seats"],
        has_toilet=bool(request.form["has_toilet"]),
        has_wifi =bool(request.form["has_wifi"]),
        has_sockets=bool(request.form["has_sockets"]),
        can_take_calls=bool(request.form["can_take_calls"]),
        coffee_price=request.form["coffee_price"]
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "The new cafe is added to the database"})


# HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(cafes).__dict__
    random_cafe.pop("_sa_instance_state")
    return jsonify(cafe=random_cafe)

@app.route("/all")
def all_cafes():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[cafe.__dict__ for cafe in cafes if cafe.__dict__.pop("_sa_instance_state")])

@app.route("/search")
def search_cafe():
    
    location = request.args.get("loc")
    
    cafes_at_location = db.session.execute(db.select(Cafe).where(Cafe.location ==location)).scalars().all()
    
    if len(cafes_at_location) >=1:
        return jsonify(cafes=[cafe.__dict__ for cafe in cafes_at_location if cafe.__dict__.pop("_sa_instance_state")])

    
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"})

@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
        
        coffee_price = request.args.get("new_price")
        
        try:
            cafe = db.session.get(Cafe, cafe_id)
            cafe.coffee_price=coffee_price
        except AttributeError:
            return jsonify(error={"Not Found": "There is no cafe with this id in the database"})
        else:
            db.session.commit()
            return jsonify(Success="Successfully updated the price")
        
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    
    api = request.args.get("api-key")
    
    if api == "TopSecretAPIKey":
            cafe_to_delete = db.session.get(Cafe, cafe_id)
            if cafe_to_delete:
                db.session.delete(cafe_to_delete)
                db.session.commit()
                return jsonify(Success="The cafe was deleted from the database")
            return jsonify(error={"Not Found": "There is no cafe with this id in the database"})
    else:
        return jsonify(error={"Authentication error": "Invalid API key"})

    
    
    
    

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
