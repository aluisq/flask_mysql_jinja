from app import cursor, app
from flask import render_template, request, redirect, url_for

@app.route("/new-ip/hur1")
def new_ip():
    return render_template('public/cadastro_maquina.html')