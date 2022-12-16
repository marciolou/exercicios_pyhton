from flask import Flask, render_template, request, redirect, session, flash, url_for
from models.pessoa import Pessoa
from models.usuario import Usuario

pessoa1 = Pessoa('Marcio', '28', '1,82')
pessoa2 = Pessoa('Joao', '22', '1,72')
pessoa3 = Pessoa('Adriano', '30', '1,80')

lista = [pessoa1, pessoa2, pessoa3]

usuario1 = Usuario('marcio','lourenco','031060')
usuario2 = Usuario('joao','casali','123456')
usuario3 = Usuario('larissa','sebold','654321')

usuarios = { 
    usuario1.nickname: usuario1,
    usuario2.nickname: usuario2,
    usuario3.nickname: usuario3
}

app = Flask(__name__)
app.secret_key = 'today'

@app.route('/listar')
def inicio():
    return render_template('lista.html', titulo = 'Lista de Pessoas', pessoas = lista)

@app.route('/casdastrar')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proximo = url_for('cadastrar')))

    return render_template('cadastro.html', titulo = 'Cadastro Pessoa')

@app.route('/criar', methods = ['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    abacate = Pessoa(nome, idade, altura)

    lista.append(abacate)

    return redirect(url_for('inicio'))

@app.route('/')
def login():
    proximo = request.args.get('proximo')
    return render_template('login.html', titulo = 'Login Usuario', proximo = proximo)

@app.route('/autenticar', methods = ['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:

        usuario = usuarios[request.form['usuario']]

        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname

            flash(usuario.nickname + ' Usuario Logado')
            proxima_pagina = request.form['proximo']
            return redirect(proxima_pagina)
    else:
        flash('Usuario ou senha invalidos')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('VOCE FOi DESCONECTADO')
    return redirect(url_for('login'))

app.run(debug=True)
