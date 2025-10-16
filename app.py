from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/funciona')
def funciona():
    return render_template('como_funciona.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/cadastro_idoso')
def cadastro_idoso():
    return render_template('cadastro_idoso.html')

@app.route('/cadastro_prestador')
def cadastro_prestador():
    return render_template('cadastro_prestador.html')

@app.route('/busca_idoso')
def busca_idoso():
    return render_template('busca_idoso.html')

@app.route('/resultado_busca_idoso')
def resultado_busca_idoso():
    return render_template('resultado_busca_idoso.html')

@app.route('/contratar_prestador')
def contratar_prestador():
    return render_template('contratar_prestador.html')


if __name__ == '__main__':
    app.run(debug=True)