from app import cursor, app
from mysql.connector import Error
from flask import render_template, request, redirect, url_for, jsonify, flash

@app.route("/delete-ip-raspberry/", methods=['GET','POST'])
def delete_ip_raspberry():   
    
    if request.method == 'POST':
        unidade = str(request.form['name_unidade'])
        hostname = str(request.form['hostname'])

        try:
            sql = (f"DELETE FROM equipments WHERE hostname ='{hostname}'")

            print(sql)

            cursor.execute(sql)

            # json = {'Status':f'MÉTODO POST ATIVO: RASPBERRY EXCLUÍDO: HOSTNAME: {hostname} -> {hospital}'}
            # return jsonify(json)

            flash(f'Raspberry: {hostname} foi deletetado com sucesso!')

            if unidade == 'HUR 1':
                return redirect(url_for('ip_rasp_hur1'))
            elif unidade == 'HGMI' :
                return redirect(url_for('ip_rasp_hgmi'))
            else:
                return redirect(url_for('ip_rasp_anexo'))

        except Error as e:
            json_error = {'Error':f' {e}'}
            return jsonify(json_error)

    else:
        request.method == 'GET'
        return redirect(url_for('index'))



@app.route("/delete-ip-machine/", methods=['GET','POST'])
def delete_ip_machine():   
    
    if request.method == 'POST':
        unidade = str(request.form['name_unidade'])
        hostname = str(request.form['hostname'])
        
        try:
            sql = (f"DELETE FROM equipments WHERE hostname ='{hostname}'")

            print(sql)

            cursor.execute(sql)

            # json = {'Status':f'MÉTODO POST ATIVO: RASPBERRY EXCLUÍDO: HOSTNAME: {hostname} -> {hospital}'}
            # return jsonify(json)

            flash(f'Raspberry: {hostname} foi deletetado com sucesso!')

            if unidade == 'HUR 1':
                return redirect(url_for('ip_hur1'))
            elif unidade == 'HGMI' :
                return redirect(url_for('ip_hgmi'))
            else:
                return redirect(url_for('ip_anexo_hur1'))

        except Error as e:
            json_error = {'Error':f' {e}'}
            return jsonify(json_error)

    else:
        request.method == 'GET'
        return redirect(url_for('index'))

