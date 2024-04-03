from sqlalchemy import create_engine, text
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float


metadata_obj = MetaData()


cliente = Table(
    'cliente', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('nome', String, nullable=False),
    Column('cpf', String(9), nullable=False),
    Column('endereco', String(9))

)

conta = Table(
    'conta', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('tipo', String, nullable=False),
    Column('agencia', String, nullable=False),
    Column('num', Integer, nullable=False),
    Column('saldo', Float),
    Column('id_cliente', Integer, ForeignKey("cliente.id"), nullable=False)

)

engine = create_engine('sqlite:///:memory:', echo=True)


metadata_obj.create_all(engine)


metadata_bd_obj = MetaData()


with engine.connect() as conn:

    # Define a query de inserção
    sql_insert_conta = text(
        "insert into conta (id, tipo, agencia, num, saldo, id_cliente) values (1, 'poupanca', '0001', 11 , 5, 1)")
    conn.execute(sql_insert_conta)

    sql_insert_cliente_1 = text(
        "insert into cliente (id, nome, cpf, endereco) values (1, 'Maria', '000222', 'rua')")
    conn.execute(sql_insert_cliente_1)

    sql_insert_cliente_2 = text(
        "insert into cliente (id, nome, cpf, endereco) values (2, 'Maia', '00022', 'rua')")
    conn.execute(sql_insert_cliente_2)

    # Define a query de seleção
    sql_select_cliente = text("select * from cliente")
    sql_select_conta = text("select * from conta")

    # Executa a query e obtém o resultado
    result = conn.execute(sql_select_cliente)

    # Itera sobre o resultado e imprime os registros
    print("Clientes:")
    for row in result:
        print(row)

    sql_delete_cliente = cliente.delete()
    print("Clientes:")
    for row in result:
        print(row)

    result = conn.execute(sql_select_conta)
    print("Contas:")
    for row in result:
        print(row)
