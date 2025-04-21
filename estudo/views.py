# ROTAS E IMPORTAÇÕES SECUNDARIAS
from estudo import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/Contato/')
def novapag():
    return "Outra view"
