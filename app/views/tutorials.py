from app import app
from flask import render_template, request, redirect, url_for


@app.route("/tutorials")
def tutorials():
    return render_template('public/tutoriais.html')