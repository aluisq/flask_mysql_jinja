from app import app
from flask import render_template, request, redirect, url_for
import pygal


@app.route("/dashboard")
def dashboard():
    
        graph = pygal.Line()
        graph.title = '% Variação das Linguagens de programação ao longo dos anos.'
        graph.x_labels = ['2011','2012','2013','2014','2015','2016']
        graph.add('Python',  [15, 31, 89, 200, 356, 900])
        graph.add('Java',    [15, 45, 76, 80,  91,  95])
        graph.add('C++',     [5,  51, 54, 102, 150, 201])
        graph.add('All others combined!',  [5, 15, 21, 55, 92, 105])
        graph_data = graph.render_data_uri()

        return render_template('public/dashboard.html', graph_data= graph_data)