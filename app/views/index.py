from app import cursor, app
from flask import render_template, request, redirect, url_for

@app.route("/")
def index():
    return render_template('public/index.html')