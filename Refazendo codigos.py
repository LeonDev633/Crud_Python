from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base 
from os import system
from dataclasses import dataclass
from time import sleep
system("cls||clear")

dados = []
#Criando Banco de dados:
BD = create_engine("sqlite:///bancodedados.db")

#Conectando ao banco de dados:
Session = sessionmaker(bind=BD)
session = Session()

#Criando Tabela e Classe:
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "usuarios"
    
    #Definindo variaveis da tabela:
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("Nome", String)
    sobrenome = Column("Sobrenome", String)
    idade = Column("Idade", Integer)
    peso = Column("Peso", Float)
    altura = Column("Altura", Float)
    sexo = Column("Sexo", String)

    #Definindo atributos da classe:
    def __init__(self,nome:str, sobrenome:str, idade:int,peso:float,altura:float,sexo:str):
        self.nome = nome
        self.sobrenome=sobrenome
        self.idade=idade
        self.peso=peso
        self.altura=altura
        self.sexo=sexo

#Criando tabela de dados, no banco de dados:
Base.metadata.create_all(bind=BD)    

#Funções:
def menu_principal ():
    print("="*40)
    print(f"{"MENU":^40}")
    print("="*40)
    print(f"""
1- ADICIONAR USUÁRIO
2- CALCULAR IMC
3- DELETAR USUÁRIO""")

def imc (altura:float, peso:float):
    imc = peso/(altura*altura)
    return imc

while True:
    system("cls||clear")
    menu_principal()
    opcao1=int(input(":"))
    match (opcao1):
        case 1:
            while True:
                system("cls||clear")
                #Dados para salvamento:
                usuario = Pessoa(
                    nome=input("Nome: "),
                    sobrenome=input("Sobrenome: "),
                    idade=int(input("Idade: ")),
                    peso=float(input("Peso: ")),
                    altura=float(input("Altura: ")),
                    sexo=input("Sexo: ")
                )
                #Salvando Usuário que adicionar os dados:
                session.add(usuario)
                session.commit()
                usuario_id = usuario.id#Para receber o ID que foi gerado logo após ter sido adicionado
                print(f"ID DE REGISTRO: {usuario_id}")
                sleep(10)
                print("""
DESEJA ADICIONAR OUTRO USUÁRIO ?
1- SIM
2- NÃO\n""")
                opcao0=int(input(": "))
                if opcao0 == 2:
                    break
        case 2:
            system("cls||clear")
            print("="*40)
            print(f"{"CACULADORA DE IMC":^40}")
            print("="*40)
            usuario_id=int(input("INFORME SEU NUMERO ID PARA CONTINUAR: "))
            usuario = session.query(Pessoa).filter(Pessoa.id == usuario_id).first()#Método de pesquisa detalhada, adcionando com filtro o ID gerado
            #Após utilizando usuario especifico com base o ID chamado:
            resultado = imc(usuario.altura,usuario.peso)
            print(f"ID DIGITADO: {usuario.id}")
            print(f"Nome: {usuario.nome} {usuario.sobrenome}")
            print(f"SEU IMC: {resultado:.2f}")
            print(f"Peso: {usuario.peso}Kg")
            print(f"Altura: {usuario.altura}m")
            print(f"Idade: {usuario.idade}")
            sleep(5)
        case 3:
            id_usuario = int(input("INFORME O ID DO USUÁRIO QUE DESEJA DELETAR: "))
            usuario = session.query(Pessoa).filter_by(id = id_usuario).first()
            session.delete(usuario)
            session.commit()
            print(f"{usuario.nome} excluido com sucesso.")
            sleep(5)