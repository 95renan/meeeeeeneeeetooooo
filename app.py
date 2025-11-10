from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

# Inicialização do app Flask
app = Flask(__name__)

# Configurações principais
app.config['SECRET_KEY'] = 'dev-secret-key'  # Corrigido (antes era SECRET-KEY)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'mysql+pymysql://root:root@localhost:3306/meu_netodb?charset=utf8mb4'
)

db = SQLAlchemy(app)

# ------------------------------
# Modelo do banco de dados
# ------------------------------
class Idoso(db.Model):
    __tablename__ = 'idoso'
    idIdoso = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    cpf = db.Column(db.String(15), unique=True)
    nome = db.Column(db.String(100))
    login = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100))
    senha = db.Column(db.String(50))
    telefone = db.Column(db.String(15))
    nascimento = db.Column(db.Date)
    parentesco = db.Column(db.String(45))
    # fotoPERFIL = db.Column(db.LargeBinary)  # caso queira futuramente armazenar imagem
    endCEP = db.Column(db.String(9))
    endRUA = db.Column(db.String(100))
    endNUMERO = db.Column(db.Integer)
    endBAIRRO = db.Column(db.String(100))
    endCIDADE = db.Column(db.String(100))
    endUF = db.Column(db.String(100))
    criadoEm = db.Column(db.DateTime, nullable=False, server_default=func.now())
    

# ------------------------------
# Rotas
# ------------------------------
@app.route('/idoso/cadastrar', methods=['POST'])
def cadastrarIdoso():
    cpf = (request.form.get('cpf') or '').strip()
    nome = (request.form.get('nome') or '').strip()
    email = (request.form.get('email') or '').strip()
    senha = (request.form.get('password') or '').strip()
    telefone = (request.form.get('fone') or '').strip()
    login = (request.form.get('login') or '').strip()
    
    nascimento_str = (request.form.get('nasc') or '').strip()
    nascimento = datetime.strptime(nascimento_str, "%Y-%m-%d").date() if nascimento_str else None
    
    endCEP = (request.form.get('cep') or '').strip()
    endNUMERO = int(request.form.get('numero') or 0)
    endRUA = (request.form.get('rua') or '').strip()
    endBAIRRO = (request.form.get('bairro') or '').strip()
    endCIDADE = (request.form.get('cidade') or '').strip()
    endUF = (request.form.get('uf') or '').strip()

    login_existente = Idoso.query.filter_by(login=login).first()
    if login_existente:
        flash('Este login já está em uso. Escolha outro nome de usuário.', 'warning')
        return redirect(url_for('cadastro_idoso'))

    try:
        u = Idoso(
            cpf=cpf,
            nome=nome,
            email=email or None,
            senha=senha,
            telefone=telefone or None,
            login=login,
            nascimento=nascimento,
            endCEP=endCEP,
            endNUMERO=endNUMERO,
            endRUA=endRUA,
            endBAIRRO=endBAIRRO,
            endCIDADE=endCIDADE,
            endUF=endUF
        )
        db.session.add(u)
        db.session.commit()
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('home'))

    except IntegrityError:
        db.session.rollback()
        flash('Usuário já cadastrado com este login ou e-mail.', 'danger')
        return redirect(url_for('home'))

    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao cadastrar: {str(e)}', 'danger')
        return redirect(url_for('home'))

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login/idoso', methods=['POST'])
def login_idoso():
    login = (request.form.get('login') or '').strip()
    senha = (request.form.get('senha') or '').strip()

    # Verifica se os campos foram preenchidos
    if not login or not senha:
        flash('Por favor, informe seu login e senha.', 'warning')
        return redirect(url_for('login'))  # rota da página de login (GET)

    # Busca o idoso pelo nome de login
    user = Idoso.query.filter_by(login=login).first()

    # Verifica se o usuário existe e se a senha está correta
    if not user or user.senha != senha:
        flash('Login ou senha incorretos. Tente novamente.', 'danger')
        return redirect(url_for('login'))

    # Cria a sessão e redireciona
    session['usuario_id'] = user.idIdoso
    session['usuario_nome'] = user.nome
    flash(f'Bem-vindo(a), {user.nome}!', 'success')
    return redirect(url_for('busca_idoso'))

# Rota que realiza o logout do usuário
@app.route('/logout', methods=['GET'])
def logout():
    # Destruição da sessão
    session.pop('usuario_id', None)
    flash('Você saiu da sessão.', 'info')
    return redirect(url_for('home'))

# ------------------------------
# Páginas principais
# ------------------------------
@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/loginprestador')
def login_prestador():
    return render_template('login_prestador.html')

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

@app.route('/inicial_prestador')
def inicial_prestador():
    return render_template('inicial_prestador.html')

@app.route('/servico_aceito')
def servico_aceito():
    return render_template('servico_aceito.html')

@app.route('/servico_concluido')
def servico_concluido():
    return render_template('servico_concluido.html')


# ------------------------------
# Execução do servidor
# ------------------------------
if __name__ == '__main__':
    host = os.getenv('HOST', '127.0.0.1')
    port = int(os.getenv('PORT', '5000'))
    app.run(host=host, port=port, debug=True)
