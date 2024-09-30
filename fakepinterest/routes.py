# Importações necessárias
from fakepinterest import app, database, bcrypt
from fakepinterest.forms import FormLoguin, FormCriarConta, FormFoto, Botao
from fakepinterest.models import Usuario, Foto

from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.utils import secure_filename

import os

# Rota para a homepage
@app.route("/", methods=['GET', 'POST'])
def homepage():
    formlogin = FormLoguin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("homepage.html", form=formlogin)

# Rota para criar conta
@app.route("/criarconta", methods=['GET', 'POST'])
def criarconta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data).decode('utf-8')
        usuario = Usuario(email=form_criarconta.email.data, senha=senha, username=form_criarconta.username.data)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("criarconta.html", form=form_criarconta)

# Rota para perfil
@app.route("/perfil/<id_usuario>", methods=["GET", "POST"])
@login_required
def perfil(id_usuario):
    usuario = Usuario.query.get(int(id_usuario))
    if int(id_usuario) == int(current_user.id):
        formfoto = FormFoto()
        if formfoto.validate_on_submit():
            arquivo = formfoto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOUD_FOLDER'], nome_seguro)
            arquivo.save(caminho)
            imagem = Foto(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(imagem)
            database.session.commit()
        return render_template("perfil.html", usuario=current_user, form=formfoto)
    else:
        return render_template("perfil.html", usuario=usuario, form=None)

# Rota para logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))

# Rota para feed
@app.route('/feed')
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao.desc()).all()[:50]
    return render_template('feed.html', fotos=fotos)

# Rota para visualização de foto
@app.route('/foto/<id_usuario>/<foto>/<id_foto>', methods=['GET', 'POST'])
@login_required
def foto(id_usuario, foto, id_foto):
    usuario = Usuario.query.get(id_usuario)
    fotoo = Foto.query.get(int(id_foto))
    form = Botao()
    if form.validate_on_submit():
        if form.botao_delete.data:
            database.session.delete(fotoo)
            database.session.commit()
            return redirect(url_for('perfil', id_usuario=id_usuario))
        elif form.botao_perfil.data:
            return redirect(url_for('perfil', id_usuario=fotoo.id_usuario))
    return render_template('visualisar_foto.html', usuario=usuario, imagem=foto, form=form)
