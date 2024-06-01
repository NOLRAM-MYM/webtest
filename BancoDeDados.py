# so para criar o banco de dados nao necessario depois do projeto exixtir
from Fakepinterest import database, app
from Fakepinterest.models import Usuario, Foto

with app.app_context():
    database.create_all()
