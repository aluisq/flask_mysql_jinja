from app import cursor, app
from flask import render_template, request, redirect, url_for, jsonify, flash

@app.route("/new-hostname/", methods=["GET","POST"])
def new_hostname():
    if request.method == 'GET':
        return render_template('public/cadastro_maquina.html')
    else:
        request.method == 'POST'
        ur = request.form["ur"]
        ip = request.form["ip"]
        hostname =  request.form["hostname"]
        local = request.form["local"]
        setor = request.form["setor"]
        unidade = request.form["unidade"]
        tipo_equipamento = request.form["equipamento"]
        ramal = request.form["ramal"]
    
        # Cofirma que os campos não sejam nulos
        if unidade != 'NULL' and tipo_equipamento != 'NULL':
            # Caso seja uma máquina faz a validação
            if tipo_equipamento == 'maquinas':

                sql = (f"SELECT * FROM equipments WHERE hostname LIKE '%{hostname}%' OR ip LIKE '%{ip}%'")
                result = []
                cursor.execute(sql)
                for r in cursor:
                    result.append(r)

                if (len(result) >= 1 and result[0][3] == hostname) or (len(result) >= 1 and result[0][2] == ip):
                    flash('Esse HOSTNAME ou IP já está sendo usado por outra Máquina!')
                    # json = {'Status' : 'Já existe um uma máquina ou raspberry com esse hostname'}
                    # return jsonify(json)
                    return render_template('public/cadastro_maquina.html', color = 'warning')

                else:
                    # regra de insert
                    flash('Máquina cadastrada com sucesso!')
                    return render_template('public/cadastro_maquina.html', color = 'success')

            # Caso seja um raspberry faz uma validação
            elif tipo_equipamento == 'raspberry':

                sql = (f"SELECT * FROM raspberry WHERE hostname LIKE '%{hostname}%' OR ip LIKE '%{ip}%'")
                result = []
                cursor.execute(sql)
                for r in cursor:
                    result.append(r)

                if (len(result) >= 1 and result[0][2] == hostname) or (len(result) >= 1 and result[0][1] == ip):
                    flash('Esse HOSTNAME ou IP já está sendo usado por outro Raspberry!')
                    # json = {'Status' : 'Já existe um uma máquina ou raspberry com esse hostname'}
                    # return jsonify(json)
                    return render_template('public/cadastro_maquina.html', color = 'warning')

                else:
                    # regra de insert
                    flash('Raspberry cadastrado com sucesso!')
                    return render_template('public/cadastro_maquina.html', color = 'success')
        else:
            flash("A 'unidade' ou o 'tipo de equipamento' não foi selecionado!")
            return render_template('public/cadastro_maquina.html',color = 'warning')