from flask import Flask, render_template, request , redirect, session, flash, url_for
# import pymysql

# db = pymysql.connect(host='localhost',
#                        user='seu_user',
#                        password='seu_password',
#                        db='jogoteca')


app = Flask(__name__)
app.secret_key = 'alura'

linkdeteste = 'https://www.google.com.br/'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

usuario1 = Usuario('igor','Igor Szot','12345')
usuario2 = Usuario('luan', 'Luan Marques', '54321')
usuario3 = Usuario('Nico','Steppat','alemao')

usuarios = { usuario1.id: usuario1,
             usuario2.id: usuario2,
             usuario3.id: usuario3}

jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'Game Boy')
jogo3 = Jogo('CSGO', 'FPS', 'PC')
lista = [jogo1,jogo2,jogo3]

@app.route('/')
def index():
    return render_template('lista.html', titulo= 'jogos', jogos= lista, link=linkdeteste)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo= 'novo jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session ['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina =  request.form['proxima']
            return redirect(proxima_pagina)
    else :
        flash('Não logado, tente de novo!')
        return redirect (url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum Usuario Logado')
    return redirect(url_for('index'))

app.run(debug=True)
