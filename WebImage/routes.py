#criar rotas do site (links)
from flask import render_template, url_for, redirect, send_from_directory
from WebImage import app, database, bcrypt # o arquivo app que esta dentro da pasta __init__
from WebImage.models import Usuario, Foto
from flask_login import login_required, login_user, logout_user, current_user
from WebImage.forms import FormLogin, FormCriarConta, FormFoto
import os
from werkzeug.utils import secure_filename # tratamento do arquivo


@app.route("/", methods=["GET", "POST"]) # rota do site (homepage) decorater
def homepage():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha.encode("utf-8"), form_login.senha.data): # valida a senha do login
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("homepage.html", form=form_login) # recebe as informaçoes do fomulario do login



@app.route("/criarconta", methods=["GET", "POST"])
def criar_conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit(): #validar o email no formulario para criar conta
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data).decode("utf-8") # criptografia da senha
        usuario = Usuario(username=form_criarconta.username.data,
                          senha=senha,
                          email=form_criarconta.email.data) #formulario.campo.informaçao do campo do models
        database.session.add(usuario) #adiciona o usuario no banco de dados
        database.session.commit() #adiciona as alteraçoes no banco de dados
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("criarconta.html", form=form_criarconta)

@app.route("/uploads/<path:filename>")
def custom_static(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attechement=True)



@app.route("/perfil/<id_usuario>", methods=["GET", "POST"]) # colocando em tagas ele se transforma em variavel
@login_required # decoradores para login
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        # visualiza o perfil do usuario
        form_foto = FormFoto()
        if form_foto.validate_on_submit(): # recebe o arquivo
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            # salvar o arquivo na pasta fotos_posts
            # os.path.join(os.path.abspath(os.path.dirname(__file__)),  ,  )
            # caminho = os.path.join(app.config["UPLOAD_FOLDER"],
            #                        nome_seguro)
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                              app.config["UPLOAD_FOLDER"],
                              nome_seguro) #nesse exemplo junta o caminho da pasta e o arquivo
            arquivo.save(caminho)
            # registrar o arquivo no banco de dados
            foto = Foto(imagem=nome_seguro , id_usuario=current_user.id) # nao esquecer do caminho correto do id_usuario
            database.session.add(foto) # adciona o arquivo no banco de dados
            database.session.commit() # salva o arquivo no banco de dados

        return render_template("perfil.html", usuario=current_user, form=form_foto)

    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario=usuario, form=None) #a marcaçao de vermelho indica a variavel no html conectando com o python

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/feed")
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao.desc()).all()[:100] #exibe no feed todas as fotos em ordem de criaçao
    return render_template("feed.html", fotos=fotos)