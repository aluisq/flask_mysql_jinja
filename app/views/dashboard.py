from app import cursor, app
from flask import render_template, request, redirect, url_for
import pygal


@app.route("/dashboard")
def dashboard():

        ### Query para as Máquinas da aplicação
        query_machine = ("SELECT COUNT(*) FROM maquinas")

        cursor.execute(query_machine)

        machine = []

        ## todo comando execute do cursor ele precisa ser rodado por um for como se fosse um fetch do php ##

        for amount_machine in cursor:
                machine.append(amount_machine[0])
        
        ### Query para os Rasperry da aplicação

        query_raspberry = ("SELECT COUNT(*) FROM raspberry")

        cursor.execute(query_raspberry)

        raspberry = []

        for amount_raspberry in cursor:
                raspberry.append(amount_raspberry[0])

        ### Dados para o gráfico

        graph = pygal.Pie()
        # graph.title = 'Máquinas e Raspberry no Complexo HUR1 / HGMI'
        graph.x_labels = ['10','30','40','50']
        graph.add('Máquinas', machine)
        graph.add('Rasperry', raspberry)
        graph_data = graph.render_data_uri()

        return render_template('public/dashboard.html', graph_data= graph_data)



        
        """
        # Dados como exemplos para construção dos gráficos 
        graph = pygal.Line()
        graph.title = '% Variação das Linguagens de programação ao longo dos anos.'
        graph.x_labels = ['2011','2012','2013','2014','2015','2016']
        graph.add('Python',  [15, 31, 89, 200, 356, 900])
        graph.add('Java',    [15, 45, 76, 80,  91,  95])
        graph.add('C++',     [5,  51, 54, 102, 150, 201])
        graph.add('All others combined!',  [5, 15, 21, 55, 92, 105])
        graph_data = graph.render_data_uri()

        """