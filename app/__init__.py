from flask import Flask
import mysql.connector
from mysql.connector import Error
from flask_bootstrap import Bootstrap
import os

try:
    connection = mysql.connector.connect(host= os.getenv("HOST"),
                                         database= os.getenv("DATABASE"),
                                         user= os.getenv("USER"),
                                         password= os.getenv("PASSWORD"))

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version", db_Info)
        cursor = connection.cursor()

except Error as e:
    print("Error while connecting to MySQL", e)

# Registra as intâncias na aplicação

app = Flask(__name__)

app.config.from_object('config.Config')

bootstrap = Bootstrap(app)

#  Registra as Views

from app.views import search_ip, delete_ip, update_ip, links, doc, dashboard, index, new_ip, qr_code, tutorials

# # MOSTRA TODOS OS PARÂMETROS DO FLASK
# print(app.config['SECRET_KEY'])