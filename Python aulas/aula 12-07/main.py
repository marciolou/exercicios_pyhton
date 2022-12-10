from flask import Flask, render_template, request, redirect
from pessoa import Pessoa

pessoa1 = Pessoa('Marcio', '28', '1,82')
pessoa2 = Pessoa('Joao', '22', '1,72')
pessoa3 = Pessoa('Adriano', '30', '1,80')

lista = [pessoa1, pessoa2, pessoa3]
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', titulo = 'Lista Pessoas', pessoas = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = 'Cadastro Pessoa')

@app.route('/criar', methods = ['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    abacate = Pessoa(nome, idade, altura)

    lista.append(abacate)

    return redirect('/')


app.run(debug=True)
