from app import app
from flask import Flask, render_template

@app.route('/')
def homepage():
    return render_template("content.html")
