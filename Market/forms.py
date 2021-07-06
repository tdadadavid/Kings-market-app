from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterFrom(FlaskForm):
    username = StringField(label='Username')
    email_address = StringField(label='Email')
    password = PasswordField(label='Password')
    password1 = PasswordField(label='Confirm Password')
    submit = SubmitField(label='Create Account')
