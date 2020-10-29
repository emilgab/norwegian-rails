from app import app
from flask import Flask, render_template

nav_items = {
    "HOME":"#home",
    "BUY TICKET":"#purchase",
    "SHOW TICKETS":"#show",
    "YOUR PROFILE":"#profile",
    "ABOUT US":"#about",
    "LOG IN":"#login"
}

@app.route('/')
def homepage():
    return render_template("homepage.html", nav_items=nav_items)
