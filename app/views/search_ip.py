from app import cursor, app
from flask import render_template, request, redirect, url_for, jsonify, flash
from mysql.connector import Error

# Mostra os resultados
# print(dados)

@app.route("/search-ip/hgmi")
def ip_hgmi():
   
        #QUERY ALTERADA PARA TESTE
        sql = ("SELECT id, ur, ip, hostname, unidade, local, setor, ramal FROM equipments WHERE unidade = 'HGMI' AND raspberry LIKE 'N%' ")
        cursor.execute(sql)
        dados = []
        unidade = "HGMI"

        for (id, ur, ip, hostname, unidade, local, setor, ramal) in cursor:
            dados.append({"id": id, "ur": ur, "ip": ip, "hostname": hostname, "unidade" : unidade, "local": local, "setor": setor, "ramal": ramal })

        # print(dados)
        return render_template('public/maquinas.html', dados = dados, unidade = unidade)

@app.route("/search-ip/hur1")
def ip_hur1():

    sql = ("SELECT id, ur, ip, hostname, unidade, local, setor, ramal FROM equipments WHERE unidade = 'HUR 1' AND raspberry LIKE 'N%' ")
    cursor.execute(sql)
    dados = []
    unidade = "HUR 1"

    for (id, ur, ip, hostname, unidade, local, setor, ramal) in cursor:
        dados.append({"id":id, "ur": ur, "ip": ip, "hostname": hostname, "unidade" : unidade, "local": local, "setor": setor, "ramal": ramal })

    # print(dados)
    return render_template('public/maquinas.html', dados = dados, unidade = unidade)

@app.route("/search-ip/anexo-hur1")
def ip_anexo_hur1():

    sql = ("SELECT id, ur, ip, hostname, unidade, local, setor, ramal FROM equipments WHERE unidade = 'ANEXO' AND raspberry LIKE 'N%' ")
    cursor.execute(sql)
    dados = []
    unidade = "ANEXO"

    for (id, ur, ip, hostname, unidade, local, setor, ramal) in cursor:
        dados.append({ "id": id, "ur": ur, "ip": ip, "hostname": hostname, "unidade" : unidade, "local": local, "setor": setor, "ramal": ramal })

    # print(dados)
    return render_template('public/maquinas.html', dados = dados, unidade = unidade) 

@app.route("/search-ip/raspberry-hur1")
def ip_rasp_hur1():

    sql = ("SELECT id, ip, hostname, unidade, local, setor FROM equipments WHERE unidade = 'HUR 1' AND raspberry LIKE 'S%'")
    cursor.execute(sql)
    dados = []
    unidade = "HUR 1"

    for (id, ip, hostname, unidade, local, setor) in cursor:
        dados.append({"id": id, "ip":ip, "hostname": hostname, "unidade": unidade, "local": local, "setor": setor})
    
    return render_template("/public/raspberry.html", dados = dados, unidade = unidade)

@app.route("/search-ip/raspberry-hgmi")
def ip_rasp_hgmi():
    sql = ("SELECT id, ip, hostname, unidade, local, setor FROM equipments WHERE unidade = 'HGMI' AND raspberry LIKE 'S%'")
    cursor.execute(sql)
    dados = []
    unidade = "HGMI"

    for (id, ip, hostname, unidade, local, setor) in cursor:
        dados.append({"id": id, "ip":ip, "hostname": hostname, "unidade": unidade, "local": local, "setor": setor})
    
    return render_template("/public/raspberry.html", dados = dados, unidade = unidade)

@app.route("/search-ip/raspberry-anexo")
def ip_rasp_anexo():
        sql = ("SELECT id, ip, hostname, unidade, local, setor FROM equipments WHERE unidade = 'ANEXO' AND raspberry LIKE 'S%'")
        cursor.execute(sql)
        dados = []
        unidade = "ANEXO"

        for (id, ip, hostname, unidade, local, setor) in cursor:
            dados.append({"id":id, "ip":ip, "hostname": hostname, "unidade": unidade, "local": local, "setor": setor})
        
        return render_template("/public/raspberry.html", dados = dados, unidade = unidade)