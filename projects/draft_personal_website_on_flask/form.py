from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email


class MyForm(FlaskForm):
    username = StringField(label="Name", validators=[DataRequired()])
    email = EmailField(label="Email", validators=[Email()])
    body = StringField(label="Message", validators=[DataRequired()])
    submit = SubmitField("Send")