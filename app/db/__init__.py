import os
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host= os.environ.get("HOST"),
                                         database= os.environ.get("DATABASE"),
                                         user= os.environ.get("USER"),
                                         password= os.environ.get("PASSWORD"), connection_timeout= 180)

    if connection.is_connected():
            db_Info = connection.get_server_info()
            global_connect_timeout = 'SET GLOBAL connect_timeout=180'
            global_wait_timeout = 'SET GLOBAL connect_timeout=180'
            global_interactive_timeout = 'SET GLOBAL connect_timeout=180'
            print("Connected to MySQL Server version", db_Info)
            cursor = connection.cursor()
            cursor.execute(global_connect_timeout)
            cursor.execute(global_wait_timeout)
            cursor.execute(global_interactive_timeout)
       
            connection.commit()


except Error as e:
    print("Error while connecting to MySQL: ", e)
