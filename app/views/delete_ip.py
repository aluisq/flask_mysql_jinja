from app import cursor, app
from mysql.connector import Error
from flask import render_template, request, redirect, url_for, jsonify, flash

@app.route("/delete-ip-raspberry/", methods=['GET','POST'])
def delete_ip_raspberry():   
    
    if request.method == 'POST':
        hospital = request.form['name_hospital']
        hostname = request.form['hostname']

        try:
            sql = (f"DELETE FROM raspberry WHERE hostname = {hostname}")

            cursor.execute(sql)

            # json = {'Status':f'MÉTODO POST ATIVO: RASPBERRY EXCLUÍDO: HOSTNAME: {hostname} -> {hospital}'}
            # return jsonify(json)

            flash(f'Raspberry: {hostname} foi deletetado com sucesso!')

            if hospital == 'HUR 1':
                return redirect(url_for('ip_rasp_hur1'))
            elif hospital == 'HGMI' :
                return redirect(url_for('ip_rasp_hgmi'))
            else:
                return redirect(url_for('ip_rasp_anexo'))

        except Error as e:
            json_error = {'Error':f' {e}'}
            return jsonify(json_error)

    else:
        request.method == 'GET'
        return redirect(url_for('index'))

