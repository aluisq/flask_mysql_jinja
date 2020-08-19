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