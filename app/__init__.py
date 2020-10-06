import os
from datetime import timedelta
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from app.db import cursor

# instanciando a aplicação FLASK

app = Flask(__name__)

# Pega as configurações apartir de um objeto chamado config 

app.config.from_object('config.Config')

# Coloca um temporizador de sessao 

@app.before_request
def before_request():
    session.permanent = True

# Instancia as demais tecnologias na aplicação

login_manager = LoginManager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

# Registra os models

from app.models import usersModel

#  Registra as Views

from app.views import search_ip, delete_ip, update_ip, links, doc, dashboard, index, new_ip, qr_code, tutorials, users, adm

# Cria o banco 
db.init_app(app)
db.create_all()

# # MOSTRA TODOS OS PARÂMETROS DO FLASK
# print(app.config['SECRET_KEY'])