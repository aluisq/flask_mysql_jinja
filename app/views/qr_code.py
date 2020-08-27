from app import cursor, app
from flask import render_template, request, redirect, url_for

@app.route("/qr-code")
def qr_code():
    return render_template('public/qr_code.html')