# Criar as rotas do nosso site (os links)

from fakepinterest import *

from flask import render_template, url_for, redirect
'''- O render_template que renderisa os arquivos da pasta templates
-O url_for pemite que dentro do htlm possamos puxar o link de cada página pelo nome da função'''

from flask_login import login_required, login_user, logout_user, current_user    # Essa Função vai servir para fazer uma exigência para usuario entrar na parte de perfil

from fakepinterest.forms import *           # Para podermos inserir os formulários dentro do html
from fakepinterest.models import *

import os
from werkzeug.utils import secure_filename      # Para criarmos um nome segura para a foto


@app.route("/", methods=['GET', 'POST'])
def homepage():
    # vamos enviar para dentro do html a variavel 'form'
    formlogin = FormLoguin()

    # Verificanodo se o login deu tudo certo
    if formlogin.validate_on_submit():
        # Encontrando o uduário dentro do banco de dados
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()

        # Verifica se encontrou o usuario
        if usuario:
            # Verifica se a senha que ele passou esta correra
            if bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
                login_user(usuario)  # fazendo login

                return redirect(url_for("perfil", id_usuario=usuario.id))

    return render_template("homepage.html", form=formlogin)

@app.route("/criarconta", methods=['GET', 'POST'])
def criarconta():
    form_criarconta = FormCriarConta()      # vamos enviar para dentro do html a variavel 'form'


    if form_criarconta.validate_on_submit():        # Verificando se o fromulário é válido

        senha = bcrypt.generate_password_hash(form_criarconta.senha.data)   # Cripitografando a senha antes de criar o usuario
        # Configurando usuario para inserir na tabela
        usuario = Usuario(email=form_criarconta.email.data, senha=senha, username=form_criarconta.username.data)
        database.session.add(usuario)   # Inserindo o usuario dentro do banco de dados
        database.session.commit()
        # Redirecinado agora o usuario para sua conta, antes de redirecionar, precisamos fazero o login, pois nossa função exige isso
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("criarconta.html", form=form_criarconta)


@app.route("/perfil/<id_usuario>", methods=["GET", "POST"])
@login_required
def perfil(id_usuario):

    # Verificando em qual perfil o usuario esta
    if int(id_usuario) == int(current_user.id):
        # Usuario esta no propio perfil
        usuario = Usuario.query.get(int(id_usuario))

        # FORMULÁRIO DE FOTO
        formfoto = FormFoto()

        if formfoto.validate_on_submit():   #Verifica se o usuário enviou uma foto

            # precisamos tratar o arquivo
            arquivo = formfoto.foto.data
            nome_seguro = secure_filename(arquivo.filename)

            # Salvar a foto dentro da pasta fotos_posts
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                       app.config['UPLOUD_FOLDER'], nome_seguro)
            arquivo.save(caminho)

            # Salvar o nome da foto no banco de dados
            imagem = Foto(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(imagem)
            database.session.commit()

        return render_template("perfil.html", usuario=current_user, form=formfoto)

    else:
        # O usuario esta no perfil de outra pessoa
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario=usuario, form=None)


@app.route('/logout')
def logout():
    # Deslogar o usuario
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/feed')
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao.desc()).all()[:50]

    return render_template('feed.html', fotos=fotos)
