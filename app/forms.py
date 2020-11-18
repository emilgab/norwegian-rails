from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,IntegerField,SelectField,RadioField,SelectMultipleField,widgets
from wtforms.fields.html5 import DateField
from wtforms import validators
from datetime import datetime

stations = ["Oslo","Fredrikstad","Halden","Bergen","Tromsø","Stavanger","Molde","Kristiansand","Lillehammer"]
stations.sort()
destinations = [(x,x) for x in stations]

class Login(FlaskForm):

    username = StringField(u"Username:",validators=[validators.DataRequired()])
    password = PasswordField(u"Password:",validators=[validators.DataRequired()])
    submit = SubmitField('Log in')

class QuickRegister(FlaskForm):
    username = StringField(u"Username:",validators=[validators.DataRequired()])
    fullname = StringField(u"Full name:",validators=[validators.DataRequired()])
    password = PasswordField(u"Password:",validators=[validators.DataRequired()])
    repeat_password = PasswordField(u"Repeat password:",validators=[validators.DataRequired()])
    submit = SubmitField("Register")

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class PurchaseTicket(FlaskForm):
    start_station = SelectField(u"Start station:", choices=destinations, validators=[validators.DataRequired()])
    end_station = SelectField(u"End station:", choices=destinations, validators=[validators.DataRequired()])
    travel_date = DateField(u"Travel date:", format="%d/%m/%Y", default=datetime.today, validators=[validators.DataRequired()])
    number_of_passengers = IntegerField(u"Passengers:", validators=[validators.DataRequired()])
    seat_reservation = RadioField('Seat reservation',choices=[
                        ('None','No reservations'),
                        ('Wheelchair space','Wheelchair space'),
                        ('Comfort cart seat','Comfort cart seat'),
                        ('Sleeping Quarters','Sleeping Quarters')
                        ], default='None', validators=[validators.DataRequired()])
    add_ons = MultiCheckboxField(choices = [
                        ('Food serving: Chicken','Food serving: Chicken'),
                        ('Food serving: Fish','Food serving: Fish and sides'),
                        ('Bring your dog onboard','Bring your dog onboard'),
                        ('Bring your ski equipment','Bring your ski equipment')
    ])
    submit = SubmitField("Go to payment")

class EntryAuth(FlaskForm):
    entrypassword = PasswordField(u"Entry password:", validators=[validators.DataRequired()])
    submit = SubmitField("Go to site")

class DeleteTicket(FlaskForm):
    ticket_serial = StringField(u"",validators=[validators.DataRequired()])
    submit = SubmitField("Delete ticket")
