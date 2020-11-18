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
    password_hash = db.Column(db.String, unique=False)
    fullname = db.Column(db.String, unique=False)

    def __init__(self,username,password,fullname):
        self.username=username
        self.password_hash=generate_password_hash(password)
        self.fullname=fullname

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

class Ticket(db.Model):
    __tablename__ = u"tickets"
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String, unique=False)
    username = db.Column(db.String, unique=False)
    fullname = db.Column(db.String, unique=False)
    start_station = db.Column(db.String, unique=False)
    end_station = db.Column(db.String, unique=False)
    date = db.Column(db.String, unique=False)
    passengers = db.Column(db.String, unique=False)
    seat_reservation = db.Column(db.String, unique=False)
    add_ons = db.Column(db.String, unique=False)
    ticket_serial = db.Column(db.String, unique=True)
    path_to_qr = db.Column(db.String, unique=False)

    def __init__(self, userid, username, fullname, start_station, end_station, date, passengers, seat_reservation, add_ons, ticket_serial, path_to_qr):
        self.userid = userid
        self.username = username
        self.fullname = fullname
        self.start_station = start_station
        self.end_station = end_station
        self.date = date
        self.passengers = passengers
        self.seat_reservation = seat_reservation
        self.add_ons = add_ons
        self.ticket_serial = ticket_serial
        self.path_to_qr = path_to_qr
