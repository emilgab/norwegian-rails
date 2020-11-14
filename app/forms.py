from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,DateTimeField,IntegerField,validators
from datetime import datetime

class Login(FlaskForm):

    username = StringField(u"Username:")
    password = PasswordField(u"Password:")
    submit = SubmitField('Log in')

class PurchaseTicket(FlaskForm):
    start_station = StringField(u"Start station:", validators=[validators.DataRequired()])
    end_station = StringField(u"End station:", validators=[validators.DataRequired()])
    travel_date = DateTimeField(u"Travel date:", format="%d/%m/%Y", default=datetime.today, validators=[validators.DataRequired()])
    number_of_passengers = IntegerField(u"Passengers:", validators=[validators.DataRequired()])
    submit = SubmitField("Go to payment")
