from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField,SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(message="The field is empty")])
    location = StringField('Cafe location on Google Maps(URL)', validators=[DataRequired(message="The field is empty"), URL(message="Please, enter the valid URL address.")])
    open = TimeField('Opens', validators=[DataRequired()])
    close = TimeField('Closes', validators=[DataRequired()])
    coffee = SelectField('Coffee rating', validators=[DataRequired()], choices=["☕️","☕️☕️","☕️☕️☕️","☕️☕️☕️☕️","☕️☕️☕️☕️☕️"])
    wifi = SelectField('WiFi Strength', validators=[DataRequired()], choices=["✘","💪","💪💪","💪💪💪","💪💪💪💪","💪💪💪💪💪"])
    power = SelectField('Power Socket Availability', validators=[DataRequired()], choices=["🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌🔌"])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='\n',encoding='utf-8') as csv_file:
            new_cafe=csv.writer(csv_file)
            new_cafe.writerow([form.cafe.data, form.location.data, form.open.data, form.close.data, form.coffee.data, form.wifi.data, form.power.data])
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
