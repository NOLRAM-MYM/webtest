# pip install flask-sqlalchemy
# pip install flask-login flask-bcrypt

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__) #cliar uma aplicação
# if os.getenv("DEBUG") == 0: # para colocar o banco de dados online
#     link_BD = os.getenv("DATABASE_URL")
# else:
#     link_BD = "sqlite://comunidade.db"
# somente uma vez para criar as tabelas do banco de dados no render
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://banco_webimage_user:UYlGav9KGWuYrpCKdkxrsQkGTVziH8C9@dpg-cpdfo4dds78s73egq480-a.oregon-postgres.render.com/banco_webimage"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL") #conrigurar dentro do render database o nome do link interno
app.config["SECRET_KEY"] = "c179ad01ab8a2855afd8724d01d43286" #senha de criptografia do site
app.config["UPLOAD_FOLDER"] = "static/fotos_posts" # configuraçao para receber uploads de arquivos ou nesse caso fotos
#app.config["UPLOAD_FOLDER"] = "/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app) # criptografia de senhas
login_manager = LoginManager(app)
login_manager.login_view = "homepage" #direcionamento do login


from WebImage import routes # as importacoes de outros arquivos tem que ficar no final como organizaçao