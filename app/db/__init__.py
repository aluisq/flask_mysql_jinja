import os
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host= os.environ.get("HOST"),
                                         database= os.environ.get("DATABASE"),
                                         user= os.environ.get("USER"),
                                         password= os.environ.get("PASSWORD"))

    if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version", db_Info)
            cursor = connection.cursor()

except Error as e:
    print("Error while connecting to MySQL: ", e)
