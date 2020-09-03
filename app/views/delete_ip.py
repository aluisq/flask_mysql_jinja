from app import cursor, app
from flask import render_template, request, redirect, url_for, jsonify

@app.route("/delete-ip-raspberry/", methods=['GET','POST'])
def delete_ip_raspberry():   
    
    if request.method == 'POST':
        hospital = request.form['name_hospital']
        hostname = request.form['hostname']

        json = {'Status':f'MÉTODO POST ATIVO: RASPBERRY EXCLUÍDO: HOSTNAME: {hostname} -> {hospital}'}
        return jsonify(json)

    else:
        request.method == 'GET'
        return redirect(url_for('index'))




# @app.route("/delete-ip/hur1", methods=['POST'])
# def delete_ip_hur1():
    

#     hospital = request.form['name_hospital']

#     print(hospital)

#     json = {'Status':'MÉTODO POST ATIVO: RASPBERRY EXCLUÍDO -> HUR1'}
#     return jsonify(json)

# @app.route("/delete-ip/anexo", methods=['POST'])
# def delete_ip_anexo():
    

#     hospital = request.form['name_hospital']

#     print(hospital)

#     json = {'Status':'MÉTODO POST ATIVO: RASPBERRY EXCLUÍDO -> ANEXO'}
#     return jsonify(json)


# @app.route("/delete-ip/hgmi", methods=['POST'])
# def delete_ip_hgmi():
    

#     hospital = request.form['name_hospital']

#     print(hospital)

#     json = {'Status':'MÉTODO POST ATIVO: RASPBERRY EXCLUÍDO -> HGMI'}
#     return jsonify(json)
