from app import cursor, app
from flask import render_template, request, redirect, url_for

@app.route("/new-hostname/")
def new_hostname():
    return render_template('public/cadastro_maquina.html')