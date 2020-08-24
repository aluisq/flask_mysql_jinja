from app import app
from flask import render_template, request, redirect, url_for

@app.route('/doc')
def doc():
    return render_template('public/doc.html')

@app.route('/doc/teste')
def doc_pdf():
    return send_file('static/pdf/teste.pdf')
