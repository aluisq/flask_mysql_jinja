from app import cursor, app
from flask import render_template, request, redirect, url_for, jsonify, flash
from mysql.connector import Error

@app.route("/new-hostname/", methods=["GET","POST"])
def new_hostname():
    if request.method == 'GET':
        return render_template('public/cadastro_maquina.html')
    else:
        request.method == 'POST'
        ur = request.form["ur"].upper().strip()
        ip = request.form["ip"].strip()
        hostname =  request.form["hostname"].upper().strip()
        local = request.form["local"].upper().strip()
        setor = request.form["setor"].upper().strip()
        unidade = request.form["unidade"].strip()
        tipo_equipamento = request.form["equipamento"].strip()
        ramal = request.form["ramal"].strip()
    
        # Cofirma que os campos não sejam nulos
        if unidade != 'NULL' and tipo_equipamento != 'NULL':

            # Caso seja uma máquina 
            if tipo_equipamento == 'maquinas':

                    try:
                        sql = (f"INSERT INTO equipments (ur, ip, hostname, unidade, local, setor, ramal, raspberry) VALUES ('{ur}' ,'{ip}', '{hostname}','{unidade}', '{local}', '{setor}', '{ramal}', 'N');")
                        print(sql)
                        cursor.execute(sql)
                        flash('Máquina cadastrada com sucesso!', "success")
                        return render_template('public/cadastro_maquina.html')
                     
                    except Error as e:
                        # json_error = {'Error':f' {e}'}
                        flash(f'Error -  Duplicidade de registro : {e}', 'warning')
                        return render_template('public/cadastro_maquina.html')

            # Caso seja um raspberry
            elif tipo_equipamento == 'raspberry':
                
                try:
                    sql = (f"INSERT INTO equipments (ip, hostname, unidade, local, setor, ramal, raspberry) VALUES ('{ip}', '{hostname}','{unidade}', '{local}', '{setor}','{ramal}', 'S');")
                    print(sql)
                    cursor.execute(sql)
                    flash('Raspberry cadastrado com sucesso!', "success")
                    return render_template('public/cadastro_maquina.html')

                except Error as e:
                    # json_error = {'Error':f' {e}'}
                    flash(f'Error -  Duplicidade de registro : {e}', "warning")
                    return render_template('public/cadastro_maquina.html')

            else:
                flash('O equipamento não foi cadastrado, verifique se os dados inseridos estão corretos.', "danger")
                return render_template('public/cadastro_maquina.html')
        else:
            flash("A 'unidade' ou o 'tipo de equipamento' não foi selecionado!", "warning")
            return render_template('public/cadastro_maquina.html')