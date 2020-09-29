import datetime
from app import app, db
from app.models.usersModel import User
from app.helpers.authentication import Auth
from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user

@app.route("/login", methods=['GET','POST'])
def login():

    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        
        user = User.query.filter_by(login=login).first()

        if not (user and user.verify_password(password)):
            flash('Login/Password inválido')
            return render_template('public/login.html')
        else:
            payload = {
                    "id" : user.id,
                    "login" : user.login,
                    "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
                    }
            token = Auth.create(payload)
            print(token)
            print(Auth.checked(token))
            if user.admin is True:
                login_user(user)
                session.permanent = True
                return redirect(url_for('index'))
            else:
                login_user(user)
                session.permanent = True
                return redirect(url_for('index'))
    else:
        return render_template('public/login.html')
    
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
