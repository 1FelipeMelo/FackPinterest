# Criar a estrutura do banco de dados
from fakepinterest import database, login_maneger
from datetime import datetime
from flask_login import UserMixin   # Esse é o que define qual class vai gerenciar o login

# Quando vai trabalhar com usuários, precisamos obrigatoriamente definir a próxima função,
# onde vamos procurar um usuário dentro do banco de dados.
@login_maneger.user_loader
def login_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


# Criando as tabelas do bandco de dados
# criar subclass database.Model, que é o modelo que o banco de dados entende e conseguimos qriar as tabelas
class Usuario(database.Model, UserMixin):
    # Criando informações do usuário:
    # o id precisa ser uníco
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)

    # A foto é o uníco campo que não vai ser uma coluna, pois ela é uma instância da classe foto
    fotos = database.relationship("Foto", backref="usuario", lazy=True)


class Foto(database.Model):
    # Criando informações da Foto:

    # o id precisa ser uníco
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, default=datetime.utcnow(), nullable=False)

    # para fazer relação com o usuario
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)

