from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from os import system
from time import sleep

def tempo_limpeza():
    system("cls||clear")
    sleep(5)

def Menu():
    print("""
1- CRIAR CONTA
2- EFETUAR LOGIN
3- ESQUECI A SENHA
""")

def senha ():
    while True:
        senha = int(input("Senha: "))
        senhaII= int(input("Digite a senha novamente: "))
        if senhaII == senha:
            break
        print("As senhas precisam ser iguais.")
        tempo_limpeza()
    return senha

BD = create_engine("sqlite:///bibbo.db")
Session = sessionmaker(bind = BD)
session = Session()
Base = declarative_base()

class Criando_login(Base):
    __tablename__ = "Usuários"

    id = Column("Id", Integer,primary_key=True, autoincrement=True)
    email = Column("Email", String)
    nome = Column("Nome", String)
    sobrenome = Column("Sobrenome", String)
    dia = Column("Data", Integer)
    mes = Column("Mês", Integer)
    ano = Column("Ano", Integer)
    senha = Column("Senha", Integer)

    def __init__(self,email:str, nome:str,sobrenome:str, dia:int, mes:int,ano:int, senha:int):
        self.email = email
        self.nome = nome
        self.sobrenome = sobrenome
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.senha = senha

Base.metadata.create_all(bind=BD)


while True:
    while True:
        Menu()
        opcao = int(input(": "))
        if opcao == 1 or 2 or 3:
            tempo_limpeza()
            break
    match (opcao):
        case 1:
            dados=[]
            usuario = Criando_login(
                nome = input("Nome: "),
                sobrenome = input("Sobrenome: "),
                email = input("Email: "),
                senha= senha(),
                dia = int(input("")), mes=int(input("/ ")), ano = int(input("/ "))               
            )
            dados.append(usuario)
            for dado in dados:
                print(dado)
                
                