from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,DateTimeField,IntegerField,SelectField
from wtforms import validators
from datetime import datetime

stations = ["Oslo","Fredrikstad","Halden","Bergen","Tromsø","Stavanger","Molde","Kristiansand","Lillehammer"]
stations.sort()
destinations = [(x,x) for x in stations]

class Login(FlaskForm):

    username = StringField(u"Username:")
    password = PasswordField(u"Password:")
    submit = SubmitField('Log in')

class PurchaseTicket(FlaskForm):
    start_station = SelectField(u"Start station:", choices=destinations, validators=[validators.DataRequired()])
    end_station = SelectField(u"End station:", choices=destinations, validators=[validators.DataRequired()])
    travel_date = DateTimeField(u"Travel date:", format="%d/%m/%Y", default=datetime.today, validators=[validators.DataRequired()])
    number_of_passengers = IntegerField(u"Passengers:", validators=[validators.DataRequired()])
    submit = SubmitField("Go to payment")
