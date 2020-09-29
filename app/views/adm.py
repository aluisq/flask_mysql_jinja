from app import app, db
from app.models.usersModel import User
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/admin/register", methods=['GET','POST'])
def register_user():

    if current_user.is_authenticated and current_user.admin:

        if request.method == 'POST':
    
            first_name = request.form['first_name'].capitalize()
            last_name = request.form['last_name'].capitalize()
            email = request.form['email']
            login = request.form['login']
            password = request.form['password']
            # criar um checkbox para informar se o usuário criado é um admin.
            admin = False
            created_at = User.created_at
            updated_at = User.updated_at

            # válida se existe os dados do formulário
            if first_name and last_name and email and login and password:

                exist_login = User.query.filter_by(login=login).first()
                exist_email = User.query.filter_by(email=email).first()

                    # valida se existe login e email
                if not (exist_login and exist_email):

                    user = User(first_name,last_name,email,login,password,admin,created_at,updated_at)
                    db.session.add(user)
                    db.session.commit()

                    # incrementar página de mensagem de usuário criado
                    flash("Usuário criado com sucesso!")
                    return redirect(url_for('register_user'), "success")
                else:
                    flash("Login/Email já existe", "warning")
                    return redirect(url_for('register_user'))
            else:
                users = User.query.filter().all()
                return render_template('private/usuarios.html', users = users)
        else:
            users = User.query.filter().all()
            return render_template('private/usuarios.html', users = users)
    #teste de usuários
    elif current_user.is_authenticated:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))


@app.route('/users')
def users():
            users = User.query.filter().all()
            return render_template('private/usuarios.html', users = users)