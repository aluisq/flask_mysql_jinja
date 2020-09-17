from app import cursor, app
from flask import render_template, request, redirect, url_for, jsonify, flash
from mysql.connector import Error

@app.route("/new-hostname/", methods=["GET","POST"])
def new_hostname():
    if request.method == 'GET':
        return render_template('public/cadastro_maquina.html')
    else:
        request.method == 'POST'
        ur = request.form["ur"]
        ip = request.form["ip"]
        hostname =  request.form["hostname"].upper()
        local = request.form["local"].upper()
        setor = request.form["setor"].upper()
        unidade = request.form["unidade"]
        tipo_equipamento = request.form["equipamento"]
        ramal = request.form["ramal"]
    
        # Cofirma que os campos não sejam nulos
        if unidade != 'NULL' and tipo_equipamento != 'NULL':

            # Caso seja uma máquina 
            if tipo_equipamento == 'maquinas':

                    try:
                        sql = (f"INSERT INTO equipments (ur, ip, hostname, unidade, local, setor, ramal, raspberry) VALUES ('{ur}' ,'{ip}', '{hostname}','{unidade}', '{local}', '{setor}', '{ramal}', 'N');")
                        cursor.execute(sql)
                        flash('Máquina cadastrada com sucesso!')
                        return render_template('public/cadastro_maquina.html', color = 'success')
                     
                    except Error as e:
                        # json_error = {'Error':f' {e}'}
                        flash(f'Error -  Duplicidade de registro : {e}')
                        return render_template('public/cadastro_maquina.html', color = 'warning')

            # Caso seja um raspberry
            elif tipo_equipamento == 'raspberry':
                
                try:
                    sql = (f"INSERT INTO equipments (ip, hostname, unidade, local, setor, ramal, raspberry) VALUES ('{ip}', '{hostname}','{unidade}', '{local}', '{setor}','{ramal}', 'S');")
                    cursor.execute(sql)
                    flash('Máquina cadastrada com sucesso!')
                    return render_template('public/cadastro_maquina.html', color = 'success')

                except Error as e:
                    # json_error = {'Error':f' {e}'}
                    flash(f'Error -  Duplicidade de registro : {e}')
                    return render_template('public/cadastro_maquina.html', color = 'warning')

            else:
                flash('O equipamento não foi cadastrado, verifique se os dados inseridos estão corretos.')
                return render_template('public/cadastro_maquina.html', color = 'danger')
        else:
            flash("A 'unidade' ou o 'tipo de equipamento' não foi selecionado!")
            return render_template('public/cadastro_maquina.html',color = 'warning')