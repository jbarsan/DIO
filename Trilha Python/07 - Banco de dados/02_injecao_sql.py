import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

# id_cliente = input("Informe o id do cliente: ")

# Forma errada pois assim é possível injetar código SQL e roubar dados
# cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")

# # cliente = cursor.fetchone()
# # print(dict(cliente))

# clientes = cursor.fetchall()

# """
# A o executar este código como no exemplo abaixo, é possível obter todos os dados
# armazenados no DB.

# Ex.: 
# Informe o id do cliente: 2 OR 1=1;

# A resposta acima na execução do programa retorna todos os dados registrados no 
# SGBD.
# """
# for cliente in clientes:
#     print(dict(cliente))

id_cliente = input("Informe o id do cliente: ")

# Forma correta e que evita SQL Injections
cursor.execute("SELECT * FROM clientes WHERE id=?", (id_cliente,))
clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))
