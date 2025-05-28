from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8, message=("Password must be at least 8 characters long"))])
    submit = SubmitField(label="Log In")
