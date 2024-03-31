"""
    Primeiro programa de integração com banco de dados
    utilizando SQLAlchemy e modelo ORM

"""
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey

Base = declarative_base()


class Cliente(Base):
    """
        Esta classe representa a tabela cliente dentro
        do SQLite.
    """
    __tablename__ = "cliente"
    
    # atributos
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))

    contas = relationship("Conta", back_populates="cliente")
    
    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco})"


class Conta(Base):
    """
    Esta classe representa a tabela conta no SQLite.
    """
    __tablename__ = "conta"

    # atributos
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    saldo = Column(Float)

    cliente = relationship("Cliente", back_populates="contas") 

    def __repr__(self):
        return f"Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, num={self.num}, saldo={self.saldo})"


print(Cliente.__tablename__)
print(Conta.__tablename__)

# conexão com o banco de dados
engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)


session = Session()

juliana = Cliente(
    nome='juliana',
    cpf='155555254',
    endereco='julianam@email.com'
)

sandy = Cliente(
    nome='sandy',
    cpf='151555254',
    endereco='juanam@email.com'
    
)
patrick = Cliente(
    nome='patrick',
    cpf='141555254',
    endereco='jnam@email.com'
    
)
conta_011 = Conta(
    tipo = 'poupanca',
    agencia = '0001',
    num = 1112,
    id_cliente = 1,
    saldo = 50
    
)

# enviando para o BD (persitência de dados)
session.add_all([juliana, sandy, patrick,conta_011])

session.commit()

stmt = select(Cliente).where(Cliente.nome.in_(["juliana", 'sandy']))
print('Recuperando clientes a partir de condição de filtragem')
for user in session.execute(stmt):
    print(user)

stmt_order = select(Cliente).order_by(Cliente.nome.desc())
print("\nRecuperando info de clientes de maneira ordenada")
for result in session.execute(stmt_order):
    print(result)


stmt_order_conta = select(Conta).order_by(Conta.tipo.desc())  
print("\nRecuperando info de contas de maneira ordenada")
for result in session.execute(stmt_order_conta):
    print(result)


connection = engine.connect()

# encerrando de fato a session
session.close()
