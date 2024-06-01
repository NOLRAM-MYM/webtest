#criar a estrutura de banco de dados
from WebImage import database, login_manager # caminho do __init__
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader #caminho da pasta models
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True) # adiciona no banco de dados o id do usuario unico
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True) # unique deixa como um email unico por conta e usuario
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True) # nao cria uma coluna no banco de dados mas armazena a foto



class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png") # somente escreve no banco de dados o local onde o arquivo esta armazenado
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey("usuario.id"), nullable=False)

