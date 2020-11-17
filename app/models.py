from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

class Users(db.Model,UserMixin):
    __tablename__ = u"users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=False)
    fullname = db.Column(db.String, unique=False)

    def __init__(self,username,password,fullname):
        self.username=username
        self.password=password
        self.fullname=fullname

class Ticket(db.Model):
    __tablename__ = u"tickets"
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String, unique=False)
    username = db.Column(db.String, unique=False)
    start_station = db.Column(db.String, unique=False)
    end_station = db.Column(db.String, unique=False)
    date = db.Column(db.String, unique=False)
    passengers = db.Column(db.String, unique=False)
    seat_reservation = db.Column(db.String, unique=False)
    add_ons = db.Column(db.String, unique=False)
