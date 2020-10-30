from app import app
from flask import Flask, render_template, Markup

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
    return render_template("homepage.html", nav_items=nav_items)

@app.route('/purchase')
def purchase():
    return render_template("purchase_tickets.html", nav_items=nav_items)

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
    return render_template("login.html", nav_items=nav_items)
