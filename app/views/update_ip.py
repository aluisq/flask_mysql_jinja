from app import cursor, app
from mysql.connector import Error
from flask import render_template, request, redirect, url_for, jsonify, flash


@app.route("/update-machine", methods=['POST'])
def update_ip_machine():
    if request.method == 'POST':

        ur = request.form['ur'].upper().strip()
        ip = request.form['ip'].strip()
        hostname = request.form['hostname'].upper().strip()
        unidade = request.form['unidade'].strip()
        local = request.form['local'].upper().strip()
        setor = request.form['setor'].upper().strip()
        ramal = request.form['ramal'].strip()

        try:
            sql = (f"UPDATE equipments SET `ur`='{ur}', `ip`='{ip}', `unidade`='{unidade}', `local`='{local}', `setor`='{setor}', `ramal`='{ramal}' WHERE `hostname`='{hostname}' ")

            print(sql)

            cursor.execute(sql)

            # json = {'Status':f'MÉTODO POST ATIVO: RASPBERRY EXCLUÍDO: HOSTNAME: {hostname} -> {hospital}'}
            # return jsonify(json)

            flash(f'Máquina: {hostname} foi atualizada com sucesso!', "success")
        

            if unidade == 'HUR 1':
                return redirect(url_for('ip_hur1'))
            elif unidade == 'HGMI' :
                return redirect(url_for('ip_hgmi'))
            else:
                unidade == 'ANEXO'
                return redirect(url_for('ip_anexo_hur1'))

        except Error as e:
                # json_error = {'Error':f' {e}'}
                # return jsonify(json_error)

                flash(f'Não foi possível atualizar a máquina: {hostname}! -  Error : {e}', "warning")

                if unidade == 'HUR 1':
                    return redirect(url_for('ip_hur1'))
                elif unidade == 'HGMI' :
                    return redirect(url_for('ip_hgmi'))
                else:
                    unidade == 'ANEXO'
                    return redirect(url_for('ip_anexo_hur1'))
                

    else:
        request.method == 'GET'
        if unidade == 'HUR 1':
            return redirect(url_for('ip_hur1'))
        elif unidade == 'HGMI' :
            return redirect(url_for('ip_hgmi'))
        else:
            return redirect(url_for('ip_anexo_hur1'))
