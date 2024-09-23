# Criar os fomularios do nosso site

# A Class que vai da herança para as Classes
from flask_wtf import FlaskForm

# Essas Class servem para definir o tipo de cada coluna da tabela
from wtforms import StringField, PasswordField, SubmitField, FileField

# Aqui temos validadores que presisamos para o formularios
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

# Vamos precisar fazer uma requisição dentro do banco de dados de usuarios, por isso estamos importadno a tabela
from fakepinterest.models import Usuario



class FormLoguin(FlaskForm):
    #Formulario de loguin
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confiramcao = SubmitField("Fazer Login")

    # Verificar se o E-mail não esta cadastrado
    def validate_email(self, email):

        # Buscando E-mail que o usuario preencheu dentro do banco de dados
        usuario = Usuario.query.filter_by(email=email.data).first()
        print(usuario)
        # Verificando Se foi encontrado um usuario cadastrado
        if not usuario:
            raise ValidationError("Usuário não cadastrado.")


class FormCriarConta(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField("Nome de usuário", validators=[DataRequired()])

    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirme sua senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    # Verificar se o E-mail já é cadastrado
    # É obrigatorio que o nome da função seja 'validete_' + 'nome da variavel que vamos verificar'
    def validate_email(self, email):
        # Buscando E-mail que o usuario preencheu dentro do banco de dados
        usuario = Usuario.query.filter_by(email=email.data).first()

        # Verificando Se foi encontrado um usuario cadastrado
        if usuario:
            raise ValidationError("O E-mail ja está cadastrado, faça login.")

    def validate_senha(self, confirmacao_senha):
        if confirmacao_senha:
            raise ValidationError('Senhas Inválida')


# Formulário para fotos
class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_enviar = SubmitField('Enviar')

