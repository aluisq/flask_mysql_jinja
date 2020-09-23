import os
from flask import Flask
from flask_bootstrap import Bootstrap
from app.db import cursor

app = Flask(__name__)

app.config.from_object('config.Config')

bootstrap = Bootstrap(app)

#  Registra as Views

from app.views import search_ip, delete_ip, update_ip, links, doc, dashboard, index, new_ip, qr_code, tutorials

# # MOSTRA TODOS OS PARÂMETROS DO FLASK
# print(app.config['SECRET_KEY'])