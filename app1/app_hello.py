from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "<h1>Hello World</h1>"

@app.route('/Primeira')
def hi():
    return '''
    <h1> Esta é a minha primeira tentativa com Flask. </h1>
    '''

app.run()