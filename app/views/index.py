from app import cursor, app
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
def index():
    if current_user.is_authenticated:
        return render_template('public/index.html')
    else:
        return redirect(url_for('login'))