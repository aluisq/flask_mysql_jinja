from app import app
from flask import render_template, request, redirect, url_for


@app.route("/links")
def links():
    return render_template('public/links.html')