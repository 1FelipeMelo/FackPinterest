# Importações necessárias
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from flask_bcrypt import Bcrypt

from fakepinterest.models import Usuario
from fakepinterest import app

# Inicializando Bcrypt
bcrypt = Bcrypt(app)

# Formulário de Login
class FormLoguin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confiramcao = SubmitField("Fazer Login")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError("Usuário não cadastrado.")

    def validate_senha_correta(self, senha):
        usuario = Usuario.query.filter_by(email=self.email.data).first()
        if not bcrypt.check_password_hash(usuario.senha, senha.data):
            raise ValidationError("Senha incorreta. Tente novamente.")

# Formulário de Criação de Conta
class FormCriarConta(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField("Nome de usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("O E-mail já está cadastrado, faça login.")

    def validate_senha(self, senha):
        if self.senha.data != self.confirmacao_senha.data:
            raise ValidationError("As senhas não correspondem. Tente novamente.")

# Formulário para Fotos
class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_enviar = SubmitField('Enviar')

# Formulário para Botões
class Botao(FlaskForm):
    botao_delete = SubmitField('Deletar Foto')
    botao_perfil = SubmitField('Perfil do Usuário')
