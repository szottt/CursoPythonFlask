from flask import Flask, render_template, request , redirect, session, flash, url_for
from dao import JogoDao,UsuarioDao
from models import Jogo, Usuario
import pymysql

app = Flask(__name__)
app.secret_key = 'alura'

linkdeteste = 'https://www.google.com.br/'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
MYSQL_HOST      = "localhost"
MYSQL_USER      = "root"
MYSQL_PASSWORD  = "todobancogosta@zika1391"
MYSQL_DB        = "jogoteca"
MYSQL_PORT      = "3306"

db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD,db=MYSQL_DB)

jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)

linkdeteste = 'https://www.google.com.br/'

@app.route('/')
def index():
    lista = jogo_dao.listar()
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
    # lista.append(jogo)
    jogo_dao.salvar(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
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


                #Ajustar depois com calma
                # {% if jogos %}
                #     <p>Temos {{ len(jogos) }} jogos no site</p>
                # {% else %}
                #     <p>Nenhum Jogo no Site</p>
                # {% endif %}
