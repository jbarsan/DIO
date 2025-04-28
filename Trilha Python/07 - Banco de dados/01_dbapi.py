import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
# cursor.row_factory = sqlite3.Row

# cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")

# data = ("Marilia", "marilia@email.com")
# cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
# conexao.commit()

def criar_tabela(conexao, cursor):
    """Criando tabela clientes"""
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?,?);", data
    )
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute(
        "UPDATE clientes SET nome=?, email=? WHERE id=?", data
    )
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute(
        "DELETE FROM clientes WHERE id=?", data
    )
    conexao.commit()


def inserir_muitos(conexao, cursor, dados):
    cursor.executemany(
        "INSERT INTO clientes (nome, email) VALUES (?,?);", dados
    )
    conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.row_factory = sqlite3.Row # Alterando o Row da exibição
    cursor.execute(
        "SELECT * FROM clientes WHERE id=?", (id,)
    )
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes;")

# inserir_registro(conexao, cursor, 'Pedro Henrique', 'phfolhas@email.com')
# inserir_registro(conexao, cursor, 'Carlos Dudu', 'dudu@email.com')

# atualizar_registro(conexao, cursor, 'Carlos Folha', 'dudufolha@email.com', 4)
# excluir_registro(conexao,cursor, 1)

# dados = [
#     ('Mirian', 'mirian@email.com'),
#     ('Joao Carlos', 'barsan@email.com'),
#     ('Kim Tec', 'kimtec@email.com'),
#     ('Nick Folha Pinsher', 'nickthepinsher@email.com'),
#     ('Francisca Santos', 'chicadossantos@email.com'),
#     ('Antonio Melgaço', 'toinmelgaco@email.com'),
#     ('Beatriz Santos', 'beatrizbochecha@email.com'),
# ]

# inserir_muitos(conexao, cursor, dados)

# Cliente não existe
# cliente = recuperar_cliente(cursor, 1)
# print(cliente)

# cliente = recuperar_cliente(cursor, 8)
# print(cliente)

# clientes = listar_clientes(cursor)
# for cliente in clientes:
#     print(cliente)

# cliente = recuperar_cliente(cursor, 2)
# print(dict(cliente))

cliente = recuperar_cliente(cursor, 7)
print(dict(cliente))
print(cliente["id"], cliente["nome"], cliente["email"])
print(f'Seja bem vindo ao sistema {cliente["nome"]}')

## EXEMPLOS DO CURSO ##
# def criar_tabela(conexao, cursor):
#     cursor.execute(
#         "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
#     )
#     conexao.commit()


# def inserir_registro(conexao, cursor, nome, email):
#     data = (nome, email)
#     cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
#     conexao.commit()


# def atualizar_registro(conexao, cursor, nome, email, id):
#     data = (nome, email, id)
#     cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
#     conexao.commit()


# def excluir_registro(conexao, cursor, id):
#     data = (id,)
#     cursor.execute("DELETE FROM clientes WHERE id=?;", data)
#     conexao.commit()


# def inserir_muitos(conexao, cursor, dados):
#     cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
#     conexao.commit()


# def recuperar_cliente(cursor, id):
#     cursor.execute("SELECT email, id, nome FROM clientes WHERE id=?", (id,))
#     return cursor.fetchone()


# def listar_clientes(cursor):
#     return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")


# clientes = listar_clientes(cursor)
# for cliente in clientes:
#     print(dict(cliente))

# cliente = recuperar_cliente(cursor, 2)
# print(dict(cliente))
# print(cliente["id"], cliente["nome"], cliente["email"])
# print(f'Seja bem vindo ao sistema {cliente["nome"]}')

# # dados = [
# #     ("Guilherme", "guilherme@gmail.com"),
# #     ("Chappie", "chappie@gmail.com"),
# #     ("Melaine", "melaine@gmail.com"),
# ]
# inserir_muitos(conexao, cursor, dados)
