from flask import Flask, render_template, request , redirect, session, flash, url_for, send_from_directory
from dao import JogoDao,UsuarioDao
from models import Jogo, Usuario
import pymysql
import os
import time

app = Flask(__name__)
app.secret_key = 'alura'

MYSQL_HOST      = "localhost"
MYSQL_USER      = "root"
MYSQL_PASSWORD  = "todobancogosta@zika1391"
MYSQL_DB        = "jogoteca"
MYSQL_PORT      = "3306"
UPLOAD_PATH     = r'C:\Users\Igor Szot\Documents\Cursos2020\CursoPythonFlask\app1\upload'

db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD,db=MYSQL_DB)

jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)


@app.route('/')
def index():
    lista = jogo_dao.listar()
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome, categoria, console)
    jogo = jogo_dao.salvar(jogo)

    arquivo = request.files['arquivo']
    upload_path = UPLOAD_PATH
    timestamp = time.time()
    arquivo.save(f'{upload_path}\\capa{jogo.id}-{timestamp}.jpg')
    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    jogo = jogo_dao.busca_por_id(id)
    nome_imagem = recupera_imagem(id)
    return render_template('editar.html', titulo='Editando Jogo', jogo=jogo, capa_jogo = nome_imagem)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome, categoria, console, id=request.form['id'])
    jogo_dao.salvar(jogo)

    arquivo = request.files['arquivo']
    upload_path = UPLOAD_PATH
    timestamp = time.time()
    deleta_arquivo(jogo.id)
    arquivo.save(f'{upload_path}\\capa{jogo.id}-{timestamp}.jpg')
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    jogo_dao.deletar(id)
    flash('O Jogo foi excluido com sucesso')
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Não logado, tente denovo!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))

@app.route('/upload/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('upload', nome_arquivo)

def recupera_imagem(id):
    for nome_arquivo in os.listdir(UPLOAD_PATH):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    os.remove(os.path.join(UPLOAD_PATH,arquivo))



app.run(debug=True)
