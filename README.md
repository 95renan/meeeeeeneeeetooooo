# 🧓 Meu Neto — Plataforma de Serviços para Idosos

O **Meu Neto** é uma plataforma web desenvolvida em **Flask + SQLAlchemy + MySQL**, criada para conectar **idosos** a **prestadores de serviço**, permitindo solicitar, aceitar e acompanhar serviços de forma simples, rápida e segura.

Este projeto foi desenvolvido como parte de um sistema completo de agendamentos, incluindo autenticação, cadastro, gerenciamento de usuários, painel do prestador, área do idoso e painel administrativo.

---

## 🚀 Funcionalidades Principais

### 👴 Área do Idoso
- Cadastro completo com endereço
- Login seguro com sessão
- Criação de pedidos de serviço
- Edição e cancelamento dos pedidos
- Visualização de:
  - **Meus pedidos**
  - **Pedidos de outros usuários**
- Acompanhamento do status:
  - Pendente  
  - Aceito  
  - Concluído

---

### 🛠️ Área do Prestador de Serviços
- Cadastro com informações de serviços oferecidos
- Login seguro
- Painel com três seções:
  - **Pedidos disponíveis**
  - **Pedidos aceitos**
  - **Pedidos concluídos**
- Ações disponíveis:
  - Aceitar serviço
  - Cancelar aceitação
  - Concluir serviço

---

### 🛡️ Área Administrativa
Acessada apenas por usuários com `perfil = "admin"`.

Inclui:
- Gerenciamento de usuários  
- Visualização de serviços cadastrados  
- Relatórios do sistema:
  - Total de idosos cadastrados
  - Total de prestadores cadastrados
  - Total de pedidos
  - Pedidos concluídos
  - Pedidos pendentes  

---

## 📚 Tecnologias Utilizadas

- **Python 3**
- **Flask**
- **Flask SQLAlchemy**
- **MySQL (pymysql)**
- **Bootstrap (templates HTML)**
- **Jinja2**
- **HTML / CSS / JavaScript**

---

## 🗂️ Estrutura do Projeto

/Meu Neto/
│
├── templates/ # Arquivos HTML
│ ├── index.html
│ ├── login.html
│ ├── login_prestador.html
│ ├── cadastro_idoso.html
│ ├── cadastro_prestador.html
│ ├── busca_idoso.html
│ ├── inicial_prestador.html
│ ├── admin.html
│ └── ... outros templates
│
├── static/ # CSS, imagens, JS, etc.
│
├── app.py # Código principal da aplicação Flask
│
├── README.md
│
└── requirements.txt # Dependências do projeto


---

## 🛠️ Como Executar o Projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/95renan/meeeeeeneeeetooooo.git
cd SEU_REPOSITORIO

python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt

Crie o banco:
CREATE DATABASE meu_netodb CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

Ajuste o arquivo app.py se necessário:
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/meu_netodb'

Crie as tabelas:
from app import db
db.create_all()

Execute o sistema
python app.py

Acesse no navegador:
http://127.0.0.1:5000

Para criar um usuário administrador:

UPDATE prestador_de_servico
SET perfil = 'admin'
WHERE login = 'admin';

🤝 Contribuições
Sinta-se à vontade para sugerir melhorias ou enviar pull requests.


👨‍💻 Desenvolvido por:
Renan Gilberto Siqueira Lino 