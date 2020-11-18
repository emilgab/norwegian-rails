from app import app, db
from flask import Flask, render_template, session, redirect, url_for, request
from app.models import Users, Ticket
from app.forms import Login, PurchaseTicket, QuickRegister, EntryAuth, DeleteTicket
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime
from random import randint
from sqlalchemy import asc
import qrcode
import os

nav_items = {
    "HOME":"homepage",
    "BUY TICKET":"purchase",
    "SHOW TICKETS":"show_tickets",
    "YOUR PROFILE":"profile",
    "ABOUT US":"about",
}

@app.route('/')
def homepage():
    if session.get('access_granted') == True:
        return render_template("homepage.html", nav_items=nav_items)
    else:
        return redirect(url_for('access_site'))

@app.route('/purchase', methods=['GET','POST'])
@login_required
def purchase():
    if session.get('access_granted') == True:
        form = PurchaseTicket()
        if form.validate_on_submit():
            ticket_info = {}
            if current_user.is_authenticated:
                now = datetime.now()
                ticket_serial = str(randint(100,999)) + str(now.strftime("%Y%m%d%m%s")) + str(randint(100,999))
                ticket_info["ticket_serial"] = ticket_serial
                start_station = form.start_station.data
                ticket_info["start_station"] = start_station
                end_station = form.end_station.data
                ticket_info["end_station"] = end_station
                date = str(form.travel_date.data)
                ticket_info["date"] = date
                passengers = str(form.number_of_passengers.data)
                ticket_info["passengers"] = passengers
                seat_reservation = form.seat_reservation.data
                ticket_info["seat_reservation"] = seat_reservation
                add_ons = ", ".join(form.add_ons.data)
                ticket_info["add_ons"] = add_ons
                userid = str(current_user.id)
                username = current_user.username
                ticket_info["username"] = username
                fullname = current_user.fullname
                ticket_info["fullname"] = fullname
                qr = qrcode.QRCode(version=1, box_size=10, border=2)
                qr.add_data("https://www.oslomet.no")
                qr.make(fit=True)
                if os.path.exists('app/static/img/qrcodes') == False:
                    os.makedirs('app/static/img/qrcodes')
                img = qr.make_image(fill='black', back_color='white')
                path_to_qr = url_for('static',filename=('img/qrcodes/'))
                img.save(f"app/{path_to_qr}"+'qrcode_ticket'+ticket_serial+'.png')
                path_to_qr += 'qrcode_ticket'+ticket_serial+'.png'
                new_ticket = Ticket(userid=userid,username=username,fullname=fullname,start_station=start_station,
                                    end_station=end_station,date=date,passengers=passengers,
                                    seat_reservation=seat_reservation,add_ons=add_ons, ticket_serial=ticket_serial,
                                    path_to_qr=path_to_qr)
                db.session.add(new_ticket)
                db.session.commit()
                session["ticket_info"] = ticket_info
                return redirect(url_for("ticket_purchase"))
        return render_template("purchase_tickets.html", nav_items=nav_items, form=form)
    else:
        return redirect(url_for('access_site'))

@app.route("/ticket_purchase")
@login_required
def ticket_purchase():
    return render_template("ticket_confirmation.html",nav_items=nav_items)

@app.route('/show_tickets')
@login_required
def show_tickets():
    if session.get('access_granted') == True:
        form = DeleteTicket()
        if form.validate_on_submit():
            pass
        tickets = Ticket.query.filter_by(username=current_user.username).order_by(asc(Ticket.date)).all()
        return render_template("show_tickets.html", nav_items=nav_items, tickets=tickets, form=form)
    else:
        return redirect(url_for('access_site'))

@app.route('/profile')
@login_required
def profile():
    if session.get('access_granted') == True:
        return render_template("profile.html", nav_items=nav_items)
    else:
        return redirect(url_for('access_site'))

@app.route('/about')
def about():
    if session.get('access_granted') == True:
        return render_template("about.html", nav_items=nav_items)
    else:
        return redirect(url_for('access_site'))

@app.route('/login', methods=['GET','POST'])
def login():
    if session.get('access_granted') == True:
        # forms
        form = Login()
        if form.validate_on_submit():
            try:
                user = Users.query.filter_by(username=form.username.data).first()
            except:
                pass
            try:
                if user.check_password(form.password.data) and user is not None:
                    login_user(user)
                    next = request.args.get('next')
                    if next == None or not next[0] == '/':
                        next = url_for('homepage')
                    return redirect(next)
            except:
                pass
        return render_template("login.html", nav_items=nav_items, form=form)
    else:
        return redirect(url_for('access_site'))

@app.route('/register', methods=['GET','POST'])
def register():
    form = QuickRegister()
    if session.get('access_granted') == True:
        if form.validate_on_submit():
            username = form.username.data
            fullname = form.fullname.data
            if form.password.data == form.repeat_password.data:
                password = form.password.data
                new_user = Users(username=username, password=password, fullname=fullname)
                db.session.add(new_user)
                db.session.commit()
            return redirect(url_for('homepage'))
        return render_template('register.html',nav_items=nav_items, form=form)

@app.route('/logout')
@login_required
def logout():
    if session.get('access_granted') == True:
        logout_user()
        return redirect(url_for('homepage'))
    else:
        return redirect(url_for('access_site'))

@app.route('/lock', methods=['GET','POST'])
def access_site():
    form = EntryAuth()
    if form.validate_on_submit():
        if form.entrypassword.data == "oslometACIT4070":
            session['access_granted'] = True
            return redirect(url_for('homepage'))
        else:
            return redirect(url_for('access_site'))
    return render_template("accesslock.html",form=form)

@app.route('/delete_ticket', methods=['GET','POST'])
def delete_ticket():
    tickets = Ticket.query.filter_by(username=current_user.username).all()
    ticket_serial = session.get('ticket_for_delete')
    db.session.delete(ticket_serial)
    db.session.commit()
    return redirect(url_for('show_tickets'))
