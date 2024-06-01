# formularios do site pip install flask-wtf
# pip install email_validator
from flask_wtf import FlaskForm #cria formularios para o site
from wtforms import StringField, PasswordField, SubmitField, FileField # criaçao de formularios
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError # validadores
from Fakepinterest.models import Usuario #caminho da pasta e da biblioteca do site Fakepinterest.model

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()]) # dentro do validador a lista de e-mail validos
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first() # recebe as informaçoes da classe FormCriarConta no banco de dados
        if not usuario:
            raise ValidationError("Usuário inexistente, crie uma conta") # raise

class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome do usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first() # recebe as informaçoes da classe FormCriarConta no banco de dados
        if usuario:
            raise ValidationError("E-mail já cadastrado, faça login para continuar") # raise
    def validate_username(self, username): #valkidade de nome do usuario unico no banco de dados
        usuario = Usuario.query.filter_by(username=username.data).first() # recebe as informaçoes da classe FormCriarConta no banco de dados
        if usuario:
            raise ValidationError("Nome do Usuário já cadastrado") # raise

class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")