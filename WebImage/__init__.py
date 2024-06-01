# pip install flask-sqlalchemy
# pip install flask-login flask-bcrypt

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__) #cliar uma aplicação
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "c179ad01ab8a2855afd8724d01d43286" #senha de criptografia do site
app.config["UPLOAD_FOLDER"] = "static/fotos_posts" # configuraçao para receber uploads de arquivos ou nesse caso fotos

database = SQLAlchemy(app)
bcrypt = Bcrypt(app) # criptografia de senhas
login_manager = LoginManager(app)
login_manager.login_view = "homepage" #direcionamento do login


from WebImage import routes # as importacoes de outros arquivos tem que ficar no final como organizaçao