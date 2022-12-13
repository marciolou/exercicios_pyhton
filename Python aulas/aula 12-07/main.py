from flask import Flask, render_template, request, redirect, session, flash
from pessoa import Pessoa

pessoa1 = Pessoa('Marcio', '28', '1,82')
pessoa2 = Pessoa('Joao', '22', '1,72')
pessoa3 = Pessoa('Adriano', '30', '1,80')

lista = [pessoa1, pessoa2, pessoa3]
app = Flask(__name__)
app.secret_key = 'today'

@app.route('/listar')
def inicio():
    return render_template('lista.html', titulo = 'Lista de Pessoas', pessoas = lista)

@app.route('/casdastrar')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')

    return render_template('novo.html', titulo = 'Cadastro Pessoa')

@app.route('/criar', methods = ['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    abacate = Pessoa(nome, idade, altura)

    lista.append(abacate)

    return redirect('/')

@app.route('/')
def login():
    return render_template('login.html', titulo = "Login")

@app.route('/autenticar', methods = ['POST'])
def autenticar():
    if 'today' == request.form['senha']:

        session['usuario_logado'] = request.form['usuario']

        flash(session['usuario_logado'] + ' Você está logado')
        return redirect('/listar')
    else:
        flash('Senha Invalida')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] == None
    flash('VOCE FOi DESCONECTADO')
    return redirect('/')

app.run(debug=True)
