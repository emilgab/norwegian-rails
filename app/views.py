from app import app
from flask import Flask, render_template, session, redirect, url_for
from app.forms import Login, PurchaseTicket, QuickRegister, EntryAuth
from flask_login import login_user, login_required, logout_user

nav_items = {
    "HOME":"homepage",
    "BUY TICKET":"purchase",
    "SHOW TICKETS":"show_tickets",
    "YOUR PROFILE":"profile",
    "ABOUT US":"about",
    "LOG IN":"login"
}

@app.route('/')
def homepage():
    if session.get('access_granted') == True:
        return render_template("homepage.html", nav_items=nav_items)
    else:
        return redirect(url_for('access_site'))

@app.route('/purchase')
def purchase():
    if session.get('access_granted') == True:
        form = PurchaseTicket()
        return render_template("purchase_tickets.html", nav_items=nav_items, form=form)
    else:
        return redirect(url_for('access_site'))

@app.route('/show_tickets')
@login_required
def show_tickets():
    if session.get('access_granted') == True:
        return render_template("show_tickets.html", nav_items=nav_items)
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

@app.route('/login')
def login():
    if session.get('access_granted') == True:
        # forms
        form = Login()
        register = QuickRegister()
        if form.validate_on_submit():
            try:
                user.Users.query.filter_by(username=form.username.data).first()
            except:
                pass
            try:
                if user.password == form.password.data:
                    login_user(user)
                    next = request.args.get('next')
                    if next == None or not next[0] == '/':
                        next = url_for('home')
                    return redirect(next)
            except:
                pass
        return render_template("login.html", nav_items=nav_items, form=form, register=register)
    else:
        return redirect(url_for('access_site'))

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
