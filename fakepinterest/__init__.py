# Arquivo obrigatorio para o flask (com esse nome o Python vai reconhecer que é um projeto Flask)
# Ele que vamos usar para criar o app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Ajuste que vamos precisar fazer para trabalar com login e senha
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

# Configuração para criar o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///comunidade.db"

# Para as auteraçõoes funcionar na parte de login precisamos fazer mais configurações no 'app'
app.config["SECRET_KEY"] = 'f3ac9280d80a4820aa36ad32a4ca1f0d'       # Geramos uma chave de alta segurança para garantir a segurança do usuarios

# Criando variavel para que possamos indicar onde vamos armazenar as fotos postadas pelo usuario
app.config['UPLOUD_FOLDER'] = 'static/fotos_posts'

# Criando o banco de dados
database = SQLAlchemy(app)

# Variáveis para trabalhar com login
bcrypt = Bcrypt(app)
login_maneger = LoginManager(app)
login_maneger.login_view = 'homepage'   # Essa variavel que estamos definindo é para direcionar o usuario onde vai fazer o login, e nosso caso é na função homepage que definimos na rota

from fakepinterest import routes

