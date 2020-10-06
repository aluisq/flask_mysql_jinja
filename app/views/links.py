from app import app
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/links")
def links():
    
    if not current_user.is_authenticated:
                return redirect(url_for('login'))
    else:
        return render_template('public/links.html')