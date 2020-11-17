from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,IntegerField,SelectField,RadioField,SelectMultipleField,widgets
from wtforms.fields.html5 import DateField
from wtforms import validators
from datetime import datetime

stations = ["Oslo","Fredrikstad","Halden","Bergen","Tromsø","Stavanger","Molde","Kristiansand","Lillehammer"]
stations.sort()
destinations = [(x,x) for x in stations]

class Login(FlaskForm):

    username = StringField(u"Username:")
    password = PasswordField(u"Password:")
    submit = SubmitField('Log in')

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class PurchaseTicket(FlaskForm):
    start_station = SelectField(u"Start station:", choices=destinations, validators=[validators.DataRequired()])
    end_station = SelectField(u"End station:", choices=destinations, validators=[validators.DataRequired()])
    travel_date = DateField(u"Travel date:", format="%d/%m/%Y", default=datetime.today, validators=[validators.DataRequired()])
    number_of_passengers = IntegerField(u"Passengers:", validators=[validators.DataRequired()])
    seat_reservation = RadioField('Seat reservation',choices=[
                        ('none','No reservations'),
                        ('hc','Wheelchair accessible'),
                        ('comfort','Comfort cart seat'),
                        ('sleep','Sleeping quarters')
                        ], default='none', validators=[validators.DataRequired()])
    add_ons = MultiCheckboxField(choices = [
                        ('chicken','Food serving: Chicken'),
                        ('fish','Food serving: Fish'),
                        ('dog','Bring your dog'),
                        ('skis','Bring your ski equipment')
    ])
    submit = SubmitField("Go to payment")
