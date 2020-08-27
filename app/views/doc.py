from app import app
from flask import render_template, request, redirect, url_for, send_file

@app.route('/doc')
def doc():
    return render_template('public/doc.html')

@app.route('/doc/thunderbird-versao-78.x')
def doc_pdf_thunderbird():
    return send_file('static/doc/thunderbird.pdf')

@app.route('/doc/ata-de-treinamento')
def doc_treinamento():
    return send_file('static/doc/ata_treinamento.pdf')