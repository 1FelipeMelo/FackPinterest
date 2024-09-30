# Criar os fomularios do nosso site

# A Class que vai da herança para as Classes
from flask_wtf import FlaskForm

# Essas Class servem para definir o tipo de cada coluna da tabela
from wtforms import StringField, PasswordField, SubmitField, FileField

# Aqui temos validadores que presisamos para o formularios
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

# Vamos precisar fazer uma requisição dentro do banco de dados de usuarios, por isso estamos importadno a tabela
from fakepinterest.models import Usuario
from flask_bcrypt import Bcrypt
from fakepinterest import *

bcrypt = Bcrypt(app)


class FormLoguin(FlaskForm):
    #Formulario de loguin
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confiramcao = SubmitField("Fazer Login")
    usuario = Usuario.query.filter_by(email=email.data).first()
    print(bcrypt.check_password_hash(usuario.senha, senha))

    # Verificar se o E-mail não esta cadastrado
    def validate_email(self, email):

        # Buscando E-mail que o usuario preencheu dentro do banco de dados
        usuario = Usuario.query.filter_by(email=email.data).first()
        # Verificando Se foi encontrado um usuario cadastrado
        if not usuario:
            raise ValidationError("Usuário não cadastrado.")

    def validate_senha_correta(self, senha):
        usuario = Usuario.query.filter_by(email=self.email.data).first()
        # Verificar se a confirmação da senha é igual à senha
        if bcrypt.check_password_hash(usuario.senha, senha):
            raise ValidationError("As senhas não correspondem. Tente novamente.")


class FormCriarConta(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField("Nome de usuário", validators=[DataRequired()])


    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])

    print(senha == confirmacao_senha)
    botao_confirmacao = SubmitField("Criar Conta")


    # Verificar se o E-mail já é cadastrado
    # É obrigatorio que o nome da função seja 'validete_' + 'nome da variavel que vamos verificar'
    def validate_email(self, email):
        # Buscando E-mail que o usuario preencheu dentro do banco de dados
        usuario = Usuario.query.filter_by(email=email.data).first()

        # Verificando Se foi encontrado um usuario cadastrado
        if usuario:
            raise ValidationError("O E-mail ja está cadastrado, faça login.")

    # Validação da senha
    def validate_senha(self, senha):
        # Verificar se a confirmação da senha é igual à senha
        if self.senha.data != self.confirmacao_senha.data:
            raise ValidationError("As senhas não correspondem. Tente novamente.")



# Formulário para fotos
class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_enviar = SubmitField('Enviar')



class Botao(FlaskForm):
    botao_delete = SubmitField('Deletar Foto')
    botao_perfil = SubmitField('Perfil do Usuário')



