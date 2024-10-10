from os import system
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
system("cls||clear")
 
#Criando Banco de dados:
DATA_BASE=create_engine("sqlite:///meubanco.db") # Informando uma variavel para receber o caminho que leva até o banco de dados

#Criando conexão com banco de dados:
Session=sessionmaker(bind=DATA_BASE)#Iniciando sessão no Banco de dados.
session= Session()

#Criando tabela:
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    #Definição da formatação/campos da tabela:
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("Nome", String)
    email = Column("Email", String)
    senha = Column("Senha", Integer)

    #Definindo atributos da classe:
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

Base.metadata.create_all(bind=DATA_BASE)

#Salvar no banco de dados:
usuario = Usuario (nome = "Maria", email = "mariamorango@gmail.com", senha= 12345) #Facilita a identificação de dados quando atribuimos a variavel. Caso não utilize a varievel tem que obedecer a ordem.
session.add(usuario)
session.commit()

usuario = Usuario(nome = "Leonardo", email = "leozinnjr@gmail.com", senha = 12345)
session.add(usuario)
session.commit

#Listando usuarios do banco de dados:
print("\nExibindo todos os usuarios do banco de dados")
lista_usuarios = session.query(Usuario).all()

#Read
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

#delete
print("\nExcluindo um usuário.")
email_usuario=input("Informe o email do usuario para ser excluido: ")

usuario = session.query(Usuario).filter_by(email=email_usuario).first()
session.delete(usuario)
session.commit()
print("Usuario excluido com sucesso.")

#listando Usuarios com um deles excluido:
print("\nExibinda todos os usuários do banco de dados")

#Read
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

session.close()#Fechamento de conexão com bando de dados.