import os
from app import app, db
from models import *  # Isso vai importar todos os modelos

with app.app_context():
    db.create_all()
    print("✅ Banco de dados criado com sucesso!")