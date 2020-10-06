from app import cursor, app
from flask import render_template, request, redirect, url_for
from app.models.usersModel import User
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/qr-code")
def qr_code():
    if not current_user.is_authenticated:
            return redirect(url_for('login'))
    else:
        return render_template('public/qr_code.html')