from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc
import pymysql



# Inicialização do app Flask
app = Flask(__name__)

# Configurações principais
app.config['SECRET_KEY'] = 'dev-secret-key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:UIwQBHXZzDuggWvYDYRWEVRlgcpybEnO@shuttle.proxy.rlwy.net:15458/railway"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

# ------------------------------
# Modelo do banco de dados (Mantido igual)
# ------------------------------
class Idoso(db.Model):
    __tablename__ = 'idoso'
    idIdoso = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    cpf = db.Column(db.String(15), unique=True)
    nome = db.Column(db.String(100))
    login = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(50))
    telefone = db.Column(db.String(15))
    nascimento = db.Column(db.Date)
    parentesco = db.Column(db.String(45))
    # fotoPERFIL = db.Column(db.LargeBinary)
    endCEP = db.Column(db.String(9))
    endRUA = db.Column(db.String(100))
    endNUMERO = db.Column(db.Integer)
    endBAIRRO = db.Column(db.String(100))
    endCIDADE = db.Column(db.String(100))
    endUF = db.Column(db.String(2))
    criadoEm = db.Column(db.DateTime, nullable=False, server_default=func.now())
    perfil = db.Column(db.String(20))

    
class Prestador(db.Model):
    __tablename__='prestador_de_servico'
    idPrestador = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    cpf = db.Column(db.String(15), unique=True)
    nome = db.Column(db.String(100))
    login = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(50))
    telefone = db.Column(db.String(15))
    nascimento = db.Column(db.Date)
    # fotoPERFIL = db.Column(db.LargeBinary)
    endCEP = db.Column(db.String(9))
    endRUA = db.Column(db.String(100))
    endNUMERO = db.Column(db.Integer)
    endBAIRRO = db.Column(db.String(100))
    endCIDADE = db.Column(db.String(100))
    endUF = db.Column(db.String(2))
    serv1 = db.Column(db.String(45))
    serv2 = db.Column(db.String(45))
    serv3 = db.Column(db.String(45))
    comprovRes = db.Column(db.String(200))
    antecedentes = db.Column(db.String(200))
    criadoEm = db.Column(db.DateTime, nullable=False, server_default=func.now())
    perfil = db.Column(db.String(20))  # 'idoso', 'prestador', 'admin'


class Agendamento(db.Model):
    __tablename__ = 'agendamento'
    idAgendamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idIdoso = db.Column(db.Integer, db.ForeignKey('idoso.idIdoso'), nullable=False)
    # prestador só será definido quando alguém aceitar o serviço
    idPrestador = db.Column(db.Integer, db.ForeignKey('prestador_de_servico.idPrestador'), nullable=True)
    dataInicioPedido = db.Column(db.DateTime, default=func.now())
    dataInicioServico = db.Column(db.Date)
    horaDisponivel = db.Column(db.Time)
    servico = db.Column(db.String(100))
    valor = db.Column(db.Numeric(10,2))
    descricao = db.Column(db.String(500))
    aceito_por = db.Column(db.Integer, db.ForeignKey('prestador_de_servico.idPrestador'), nullable=True)
    status = db.Column(db.String(20), default="pendente")
    idoso = db.relationship("Idoso", foreign_keys=[idIdoso])
    prestador = db.relationship("Prestador", foreign_keys=[aceito_por])



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
    parentesco = (request.form.get('relationship') or '').strip()
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
            parentesco=parentesco,
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
        return redirect(url_for('login'))

    except IntegrityError:
        db.session.rollback()
        flash('Usuário já cadastrado com este login ou e-mail.', 'danger')
        return redirect(url_for('home'))

    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao cadastrar: {str(e)}', 'danger')
        return redirect(url_for('home'))

@app.route('/prestador/cadastrar', methods=['POST'])
def cadastrarPrestador():
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
    serv1 = (request.form.get('serv1') or '').strip()
    serv2 = (request.form.get('serv2') or '').strip()
    serv3 = (request.form.get('serv3') or '').strip()
    comprovRes = (request.form.get('comprovRes') or '').strip()
    antecedentes = (request.form.get('anteced') or '').strip()

    # Verifica se o login já existe
    login_existente = Prestador.query.filter_by(login=login).first()
    if login_existente:
        flash('Este login já está em uso. Escolha outro nome de usuário.', 'warning')
        return redirect(url_for('cadastro_prestador'))  # rota do formulário de cadastro

    try:
        p = Prestador(
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
            endUF=endUF,
            serv1=serv1,
            serv2=serv2,
            serv3=serv3,
            comprovRes=comprovRes,
            antecedentes=antecedentes
        )
        db.session.add(p)
        db.session.commit()

        # Usuário cadastrado com sucesso
        flash('Cadastro realizado com sucesso! Faça login para continuar.', 'success')
        return redirect(url_for('loginprestador'))  # vai para a tela de login

    except IntegrityError:
        db.session.rollback()
        flash('Usuário já cadastrado com este login ou e-mail.', 'danger')
        return redirect(url_for('loginprestador'))

    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao cadastrar: {str(e)}', 'danger')
        return redirect(url_for('cadastro_prestador'))
 
    
@app.route('/pedido/cadastrar', methods=['POST'])
def cadastrarPedido():

    # Exige usuário logado
    uid = session.get('usuario_id')
    if not uid:
        flash('Faça login para reservar.', 'warning')
        return redirect(url_for('index'))
    
    servico = (request.form.get('servico') or '').strip()
    dataInicio = (request.form.get('dataInicio') or '').strip()
    horaDisponivel = (request.form.get('horaDisponivel') or '').strip()
    valor = (request.form.get('valor') or '').strip()
    descricao = (request.form.get('descricao') or '').strip()

    # Valida campos obrigatórios
    if not servico or not dataInicio or not horaDisponivel or not valor or not descricao:
        flash('Informe tipo de serviço, data, horário e descrição.', 'warning')
        return redirect(url_for('busca_idoso'))
    
    # Converte data e horários
    try:
        data = datetime.strptime(dataInicio, '%Y-%m-%d').date()
        inicio = datetime.strptime(horaDisponivel, '%H:%M').time()
    except ValueError:
        flash('Formato de data/horário inválido.', 'danger')
        return redirect(url_for('busca_idoso'))
    
    try:
        a = Agendamento(
            idIdoso=session['usuario_id'],
            idPrestador=None,
            servico=servico,
            dataInicioServico=data,
            horaDisponivel=inicio,
            valor=valor,
            descricao=descricao
)

        db.session.add(a)
        db.session.commit()
        # >>> REDIRECIONAMENTO ATUALIZADO <<<
        flash('Pedido criado com sucesso! Abaixo, confira a lista de pedidos.', 'success')
        return redirect(url_for('busca_idoso'))
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao criar reserva: {str(e)}', 'danger')
        return redirect(url_for('busca_idoso'))
    
@app.route('/pedido/cancelar/<int:idAgendamento>', methods=['POST'])
def cancelarPedido(idAgendamento):

    usuario_id = session.get('usuario_id')

    if not usuario_id:
        flash("Faça login para continuar.", "warning")
        return redirect(url_for('login'))

    # Verifica se o pedido pertence ao usuário
    pedido = Agendamento.query.filter_by(idAgendamento=idAgendamento, idIdoso=usuario_id).first()

    if not pedido:
        flash("Você não tem permissão para cancelar este pedido.", "danger")
        # >>> REDIRECIONAMENTO ATUALIZADO <<<
        return redirect(url_for('busca_idoso'))

    try:
        db.session.delete(pedido)
        db.session.commit()
        flash("Pedido cancelado com sucesso!", "success")
    except:
        db.session.rollback()
        flash("Erro ao cancelar pedido.", "danger")

    # >>> REDIRECIONAMENTO ATUALIZADO <<<
    return redirect(url_for('busca_idoso'))

    
@app.route('/loginprestador')
def loginprestador():
    return render_template('login_prestador.html')

@app.route('/login/prestador', methods=['POST'])
def login_prestador():
    login = (request.form.get('login') or '').strip()
    senha = (request.form.get('senha') or '').strip()

    # Validação básica
    if not login or not senha:
        flash('Por favor, informe seu login e senha.', 'warning')
        return redirect(url_for('loginprestador'))

    # Busca prestador pelo login
    user = Prestador.query.filter_by(login=login).first()

    if not user or user.senha != senha:
        flash('Login ou senha incorretos. Tente novamente.', 'danger')
        return redirect(url_for('loginprestador'))

    # Cria a sessão
    session['usuario_id'] = user.idPrestador
    session['usuario_nome'] = user.nome
    session['usuario_perfil'] = user.perfil

    flash(f'Bem-vindo(a), {user.nome}!', 'success')

    # Redireciona para dashboard/admin ou inicial prestador
    if user.perfil == "admin":
        return redirect(url_for('admin_dashboard'))
    return redirect(url_for('inicial_prestador'))



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
        return redirect(url_for('login'))

    # Busca o idoso pelo nome de login
    user = Idoso.query.filter_by(login=login).first()

    # Verifica se o usuário existe e se a senha está correta
    if not user or user.senha != senha:
        flash('Login ou senha incorretos. Tente novamente.', 'danger')
        return redirect(url_for('login'))

    # Cria a sessão e redireciona
    session['usuario_id'] = user.idIdoso
    session['usuario_nome'] = user.nome
    session['usuario_perfil'] = user.perfil
    session['usuario_endCEP'] = user.endCEP
    session['usuario_endRUA'] = user.endRUA
    session['usuario_endNUMERO'] = user.endNUMERO
    session['usuario_endBAIRRO'] = user.endBAIRRO
    session['usuario_endCIDADE'] = user.endCIDADE
    session['usuario_endUF'] = user.endUF
    flash(f'Bem-vindo(a), {user.nome}!', 'success')
    if user.perfil == "admin":
        return redirect(url_for('admin_dashboard'))
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
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para acessar esta página.', 'warning')
        return redirect(url_for('login'))

    usuario_id = session.get('usuario_id')
    nome = session.get('usuario_nome')
    cep = session.get('usuario_endCEP')
    rua = session.get('usuario_endRUA')
    numero = session.get('usuario_endNUMERO')
    bairro = session.get('usuario_endBAIRRO')
    cidade = session.get('usuario_endCIDADE')
    uf = session.get('usuario_endUF')
    
    # ----------------------------------------------------
    # LÓGICA DE BUSCA DE PEDIDOS MOVIDA DE resultado_busca_idoso
    # ----------------------------------------------------
    
    # MEUS PEDIDOS
    meus_pedidos_query = (
        db.session.query(Agendamento, Idoso)
        .join(Idoso, Agendamento.idIdoso == Idoso.idIdoso)
        .filter(Agendamento.idIdoso == usuario_id)
        .order_by(db.desc(Agendamento.dataInicioPedido))
        .all()
    )

    # OUTROS PEDIDOS
    # Filtro: Mostrar apenas pedidos que não são do usuário logado (assumindo que idIdoso é o ID do solicitante)
    outros_pedidos_query = (
        db.session.query(Agendamento, Idoso)
        .join(Idoso, Agendamento.idIdoso == Idoso.idIdoso)
        .filter(Agendamento.idIdoso != usuario_id)
        .order_by(db.desc(Agendamento.dataInicioPedido))
        .all()
    )

    # LISTA FORMATADA (Meus Pedidos)
    meus = []
    for ped, user in meus_pedidos_query:
        meus.append({
            "id": ped.idAgendamento,
            "servico": ped.servico,
            "dataInicioServico": ped.dataInicioServico,
            "horaDisponivel": ped.horaDisponivel,
            "valor": ped.valor,
            "descricao": ped.descricao,
            "nome_solicitante": user.nome
        })

    # LISTA FORMATADA (Outros Pedidos)
    outros = []
    for ped, user in outros_pedidos_query:
        outros.append({
            "id": ped.idAgendamento,
            "servico": ped.servico,
            "dataInicioServico": ped.dataInicioServico,
            "horaDisponivel": ped.horaDisponivel,
            "valor": ped.valor,
            "descricao": ped.descricao,
            "nome_solicitante": user.nome
        })
    
    # Renderiza a template com todos os dados
    return render_template(
        'busca_idoso.html', 
        nome=nome, 
        cep=cep, 
        rua=rua, 
        numero=numero, 
        bairro=bairro, 
        cidade=cidade, 
        uf=uf,
        meus_pedidos=meus,     # Variável de Meus Pedidos
        outros_pedidos=outros # Variável de Outros Pedidos
    )
    

# Rota /resultado_busca_idoso foi absorvida pela /busca_idoso
# Vamos deixá-la aqui apenas para referência e remover a lógica
# @app.route('/resultado_busca_idoso')
# def resultado_busca_idoso():
#     # Essa rota não é mais necessária. Pode ser removida ou redirecionada.
#     return redirect(url_for('busca_idoso'))

@app.route('/pedido/editar/<int:id>', methods=['GET'])
def editar_pedido_form(id):
    if 'usuario_id' not in session:
        flash("Você precisa estar logado para editar o pedido.", "warning")
        return redirect(url_for('login'))

    pedido = Agendamento.query.get_or_404(id)

    # Garantir que o pedido pertence a quem está logado
    if pedido.idIdoso != session['usuario_id']:
        flash("Você não pode editar este pedido.", "danger")
        # >>> REDIRECIONAMENTO ATUALIZADO <<<
        return redirect(url_for('busca_idoso'))

    return render_template("editar_pedido.html", pedido=pedido)

@app.route('/pedido/editar/<int:id>', methods=['POST'])
def editar_pedido(id):
    pedido = Agendamento.query.get_or_404(id)

    pedido.servico = request.form.get('servico')
    pedido.dataInicioServico = datetime.strptime(request.form.get('dataInicioServico'), "%Y-%m-%d").date()
    pedido.horaDisponivel = datetime.strptime(request.form.get('horaDisponivel'), "%H:%M").time()
    pedido.valor = request.form.get('valor')
    pedido.descricao = request.form.get('descricao')

    db.session.commit()

    flash("Pedido atualizado com sucesso!", "success")
    # >>> REDIRECIONAMENTO ATUALIZADO <<<
    return redirect(url_for('busca_idoso'))

# ... (Restante das rotas: contratar_prestador, inicial_prestador, servico_aceito, servico_concluido - Mantidas iguais) ...
@app.route('/contratar_prestador')
def contratar_prestador():
    return render_template('contratar_prestador.html')

@app.route('/inicial_prestador')
def inicial_prestador():
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para acessar esta página.', 'warning')
        return redirect(url_for('login_prestador'))

    prestador_id = session['usuario_id']
    nome = session.get('usuario_nome')

    # Pedidos disponíveis COM JOIN para trazer o nome do idoso
    pedidos_disponiveis = (
        db.session.query(Agendamento, Idoso)
        .join(Idoso, Agendamento.idIdoso == Idoso.idIdoso)
        .filter(Agendamento.aceito_por.is_(None))
        .order_by(desc(Agendamento.dataInicioPedido))
        .all()
    )
    
    # Pedidos aceitos COM JOIN para trazer o nome do idoso
    pedidos_aceitos = (
        db.session.query(Agendamento, Idoso)
        .join(Idoso, Agendamento.idIdoso == Idoso.idIdoso)
        .filter(Agendamento.aceito_por == prestador_id, Agendamento.status == "aceito")
        .order_by(desc(Agendamento.dataInicioPedido))
        .all()
    )
    
    # Pedidos concluídos COM JOIN para trazer o nome do idoso
    pedidos_concluidos = (
        db.session.query(Agendamento, Idoso)
        .join(Idoso, Agendamento.idIdoso == Idoso.idIdoso)
        .filter(Agendamento.aceito_por == prestador_id, Agendamento.status == "concluido")
        .order_by(desc(Agendamento.dataInicioServico))
        .all()
    )

    return render_template(
        'inicial_prestador.html',
        nome=nome,
        pedidos_disponiveis=pedidos_disponiveis,
        pedidos_aceitos=pedidos_aceitos,
        pedidos_concluidos=pedidos_concluidos
    )

@app.route('/prestador/aceitar/<int:id>', methods=['POST'])
def aceitar_servico(id):
    if 'usuario_id' not in session:
        flash('Você precisa estar logado.', 'warning')
        return redirect('/login_prestador')

    prestador_id = session['usuario_id']
    pedido = Agendamento.query.get(id)

    if not pedido:
        flash("Serviço não encontrado.", "danger")
        return redirect('/inicial_prestador')

    if pedido.aceito_por is not None:
        flash("Esse serviço já foi aceito por outra pessoa.", "warning")
        return redirect('/inicial_prestador')

    pedido.aceito_por = prestador_id
    pedido.status = "aceito"
    db.session.commit()

    flash("Serviço aceito com sucesso!", "success")
    return redirect('/inicial_prestador')

@app.route('/prestador/cancelar/<int:id>', methods=['POST'])
def cancelar_aceitacao(id):
    if 'usuario_id' not in session:
        flash('Você precisa estar logado.', 'warning')
        return redirect('/login_prestador')

    prestador_id = session['usuario_id']
    pedido = Agendamento.query.get(id)

    if not pedido or pedido.aceito_por != prestador_id:
        flash("Operação inválida.", "danger")
        return redirect('/inicial_prestador')

    pedido.aceito_por = None
    pedido.status = "pendente"
    db.session.commit()

    flash("Aceitação cancelada.", "info")
    return redirect('/inicial_prestador')

@app.route('/prestador/concluir/<int:id>', methods=['POST'])
def concluir_servico(id):
    if 'usuario_id' not in session:
        flash('Você precisa estar logado.', 'warning')
        return redirect('/login_prestador')

    prestador_id = session['usuario_id']
    pedido = Agendamento.query.get(id)

    if not pedido or pedido.aceito_por != prestador_id:
        flash("Operação inválida.", "danger")
        return redirect('/inicial_prestador')

    pedido.status = "concluido"
    db.session.commit()

    flash("Serviço concluído com sucesso!", "success")
    return redirect('/inicial_prestador')


@app.route('/admin')
def admin_dashboard():
    # Bloqueia quem não é admin
    if session.get('usuario_perfil') != 'admin':
        flash("Acesso restrito aos administradores.", "danger")
        return redirect(url_for('home'))

    view = request.args.get('view', 'home')

    idosos = []
    prestadores = []
    servicos = []

    if view == "usuarios":
        idosos = Idoso.query.order_by(desc(Idoso.idIdoso)).all()
        prestadores = Prestador.query.order_by(desc(Prestador.idPrestador)).all()

    if view == "servicos":
        servicos = Agendamento.query.order_by(desc(Agendamento.idAgendamento)).all()

    if view == "relatorios":
        # Estatísticas gerais
        total_idosos = Idoso.query.count()
        total_prestadores = Prestador.query.count()
        total_pedidos = Agendamento.query.count()
        concluidos = Agendamento.query.filter_by(status="concluido").count()
        pendentes = Agendamento.query.filter_by(status="pendente").count()

        relatorios = {
            "total_idosos": total_idosos,
            "total_prestadores": total_prestadores,
            "total_pedidos": total_pedidos,
            "concluidos": concluidos,
            "pendentes": pendentes
        }

    return render_template(
    'admin.html',
    view=view,
    idosos=idosos,
    prestadores=prestadores,
    servicos=servicos,
    total_idosos=locals().get("total_idosos"),
    total_prestadores=locals().get("total_prestadores"),
    total_pedidos=locals().get("total_pedidos"),
    concluidos=locals().get("concluidos"),
    pendentes=locals().get("pendentes"),
    )



@app.route('/admin/usuarios')
def admin_usuarios():
    idosos = Idoso.query.all()
    prestadores = Prestador.query.all()

    return render_template(
        'admin_usuarios.html',
        idosos=idosos,
        prestadores=prestadores
    )

@app.route('/admin/servicos')
def admin_servicos():
    pedidos = Agendamento.query.order_by(Agendamento.dataInicioPedido.desc()).all()
    return render_template('admin_servicos.html', pedidos=pedidos)

@app.route('/admin/relatorios')
def admin_relatorios():
    total_idosos = Idoso.query.count()
    total_prestadores = Prestador.query.count()
    total_pedidos = Agendamento.query.count()

    concluidos = Agendamento.query.filter_by(status="concluido").count()
    pendentes = Agendamento.query.filter_by(status="pendente").count()

    return render_template(
        'admin_relatorios.html',
        total_idosos=total_idosos,
        total_prestadores=total_prestadores,
        total_pedidos=total_pedidos,
        concluidos=concluidos,
        pendentes=pendentes
    )



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