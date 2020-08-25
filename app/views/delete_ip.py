# from app import cursor, app
# from flask import render_template, request, redirect, url_for

# @app.route("/delete-ip/hur1")
# def delete_ip_hgmi():

#     ip = request.form['ipNumber']

#     sql = ("SELECT ur, ip, hospital, local, setor, ramal FROM maquinas WHERE hospital = 'HGMI' ")
#     cursor.execute(sql)
#     dados = []
#     hospital = "HGMI"

#     for (ur, ip, hospital, local, setor, ramal) in cursor:
#         dados.append({"ur": ur, "ip": ip, "hospital" : hospital, "local": local, "setor": setor, "ramal": ramal })

#     # print(dados)
#     return render_template('public/ip.html', dados = dados, hospital = hospital)