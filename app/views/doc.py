from app import app
from flask import render_template, request, redirect, url_for, send_file
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/doc')
def doc():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
         return render_template('public/doc.html')

@app.route('/doc/thunderbird-versao-78.x')
def doc_pdf_thunderbird():
    if not current_user.is_authenticated:
            return redirect(url_for('login'))
    else:
        return send_file('static/doc/thunderbird.pdf')

@app.route('/doc/ata-de-treinamento')
def doc_treinamento():
    if not current_user.is_authenticated:
            return redirect(url_for('login'))
    else:
        return send_file('static/doc/ata_treinamento.pdf')