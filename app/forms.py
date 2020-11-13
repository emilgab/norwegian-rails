from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField

class Login(FlaskForm):

    username = StringField(u"Username:")
    password = PasswordField(u"Password:")
    submit = SubmitField('Log in')
