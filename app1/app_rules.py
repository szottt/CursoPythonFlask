from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'Index'

# @app.route('/teste')
def teste():
    return 'teste'

def teste():
    return "<p> testando </p>"

def teste2():
    return "<h1> testando </h1>"

app.add_url_rule("/teste","teste",teste)
app.add_url_rule("/teste2", "teste2", teste2)

if __name__ == '__main__':
    app.run(port='3000')
