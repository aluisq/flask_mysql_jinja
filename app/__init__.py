import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from app.db import cursor

app = Flask(__name__)

app.config.from_object('config.Config')

login_manager = LoginManager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

# Registra os models

from app.models import usersModel

#  Registra as Views

from app.views import search_ip, delete_ip, update_ip, links, doc, dashboard, index, new_ip, qr_code, tutorials, users, adm


# # MOSTRA TODOS OS PARÂMETROS DO FLASK
# print(app.config['SECRET_KEY'])

db.init_app(app)
db.create_all()