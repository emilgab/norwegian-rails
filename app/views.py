from app import app
from flask import Flask, render_template, session, redirect, url_for
from app.forms import Login, PurchaseTicket, QuickRegister, EntryAuth

nav_items = {
    "HOME":"homepage",
    "BUY TICKET":"purchase",
    #"SHOW TICKETS":"show_tickets",
    #"YOUR PROFILE":"profile",
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
    form = PurchaseTicket()
    return render_template("purchase_tickets.html", nav_items=nav_items, form=form)

@app.route('/show_tickets')
def show_tickets():
    return render_template("show_tickets.html", nav_items=nav_items)

@app.route('/profile')
def profile():
    return render_template("profile.html", nav_items=nav_items)

@app.route('/about')
def about():
    return render_template("about.html", nav_items=nav_items)

@app.route('/login')
def login():
    # forms
    form = Login()
    register = QuickRegister()
    return render_template("login.html", nav_items=nav_items, form=form, register=register)

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
