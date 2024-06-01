# so para criar o banco de dados nao necessario depois do projeto exixtir
from WebImage import database, app
from WebImage.models import Usuario, Foto

with app.app_context():
    database.create_all()
