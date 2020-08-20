from app import cursor, app
from flask import render_template, request, redirect, url_for

# Mostra os resultados
# print(dados)


@app.route("/")
def index():
    return render_template('public/home.html')

@app.route("/search-ip/hgmi")
def ip_hgmi():

    sql = ("SELECT ur, ip, hospital, local, setor, ramal FROM maquinas WHERE hospital = 'HGMI' ")
    cursor.execute(sql)
    dados = []
    hospital = "HGMI"

    for (ur, ip, hospital, local, setor, ramal) in cursor:
        dados.append({"ur": ur, "ip": ip, "hospital" : hospital, "local": local, "setor": setor, "ramal": ramal })

    # print(dados)
    return render_template('public/ip.html', dados = dados, hospital = hospital)

@app.route("/search-ip/hur1")
def ip_hur1():

    sql = ("SELECT ur, ip, hospital, local, setor, ramal FROM maquinas WHERE hospital = 'HUR 1' ")
    cursor.execute(sql)
    dados = []
    hospital = "HUR 1"

    for (ur, ip, hospital, local, setor, ramal) in cursor:
        dados.append({"ur": ur, "ip": ip, "hospital" : hospital, "local": local, "setor": setor, "ramal": ramal })

    # print(dados)
    return render_template('public/ip.html', dados = dados, hospital = hospital)

@app.route("/search-ip/anexo-hur1")
def ip_anexo_hur1():

    sql = ("SELECT ur, ip, hospital, local, setor, ramal FROM maquinas WHERE hospital = 'ANEXO' ")
    cursor.execute(sql)
    dados = []
    hospital = "ANEXO"

    for (ur, ip, hospital, local, setor, ramal) in cursor:
        dados.append({"ur": ur, "ip": ip, "hospital" : hospital, "local": local, "setor": setor, "ramal": ramal })

    # print(dados)
    return render_template('public/ip.html', dados = dados, hospital = hospital) 

@app.route("/search-ip/raspberry-hur1")
def ip_rasp_hur1():

    sql = ("SELECT ip, hospital, local, setor FROM raspberry WHERE hospital = 'HUR 1' ")
    cursor.execute(sql)
    dados = []
    hospital = "HUR 1"

    for (ip, hospital, local, setor) in cursor:
        dados.append({"ip":ip, "hospital": hospital, "local": local, "setor": setor})
    
    return render_template("/public/raspberry.html", dados = dados, hospital = hospital)

@app.route("/search-ip/raspberry-hgmi")
def ip_rasp_hgmi():
    sql = ("SELECT ip, hospital, local, setor FROM raspberry WHERE hospital = 'HGMI' ")
    cursor.execute(sql)
    dados = []
    hospital = "HGMI"

    for (ip, hospital, local, setor) in cursor:
        dados.append({"ip":ip, "hospital": hospital, "local": local, "setor": setor})
    
    return render_template("/public/raspberry.html", dados = dados, hospital = hospital)

@app.route("/search-ip/raspberry-anexo")
def ip_rasp_anexo():
    sql = ("SELECT ip, hospital, local, setor FROM raspberry WHERE hospital = 'ANEXO' ")
    cursor.execute(sql)
    dados = []
    hospital = "ANEXO"

    for (ip, hospital, local, setor) in cursor:
        dados.append({"ip":ip, "hospital": hospital, "local": local, "setor": setor})
    
    return render_template("/public/raspberry.html", dados = dados, hospital = hospital)