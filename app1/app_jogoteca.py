from flask import Flask, render_template, request



app = Flask(__name__)

linkdeteste = 'https://www.google.com.br/'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'Game Boy')
jogo3 = Jogo('CSGO', 'FPS', 'PC')
jogo4 = Jogo('teste', 'rpg', 'ps4')
lista = [jogo1,jogo2,jogo3, jogo4]

@app.route('/')
def index():
    return render_template('lista.html', titulo= 'jogos', jogos= lista, link=linkdeteste)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo= 'novo jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo='jogos', jogos=lista)

app.run(debug=True)


                #Ajustar depois com calma
                # {% if jogos %}
                #     <p>Temos {{ len(jogos) }} jogos no site</p>
                # {% else %}
                #     <p>Nenhum Jogo no Site</p>
                # {% endif %}