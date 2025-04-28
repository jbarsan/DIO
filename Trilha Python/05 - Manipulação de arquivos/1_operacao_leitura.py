# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!

# Lendo o arquivo todo
arquivo = open(
    "/home/joaocarlos/Documentos/Estudos/DIO/Trilha Python/05 - Manipulação de arquivos/lorem.txt"
)

# read() carrega todo o conteúdo para a memória.
# print(arquivo.read())
# # arquivo.close()
# print('='*60)

# Lendo linha a linha
# readline() carrega somente a linha lida para a memória.
# print("Utilizando somente o print e readline()")
# print(arquivo.readline())

# print("Usando o laço for:")
# for line in arquivo.readline():
#     print(line)

# # arquivo.close()
# print('='*60)

# Lendo com while
# print("Utilizando somente o readline() no While")

# while len(line := arquivo.readline()): # perador walrus, um operador especial que realiza atribuições
#     print(line)

# # arquivo.close()
# print('='*60)

# realines() carrega linha a linha armazenando o conteúdo em uma lista
print("Utilizando somente readlines()")
print(arquivo.readlines())
print(f"\nO tipo do arquivo é: {type(arquivo.readlines())}")


arquivo.close()
