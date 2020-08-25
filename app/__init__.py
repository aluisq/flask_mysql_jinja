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
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()

except Error as e:
    print("Error while connecting to MySQL", e)

# Registra as intâncias na aplicação

app = Flask(__name__)

bootstrap = Bootstrap(app)


#  Registra as Views

from app.views import search_ip, links, doc

# # MOSTRA TODOS OS PARÂMETROS DO FLASK
# print(app.config)