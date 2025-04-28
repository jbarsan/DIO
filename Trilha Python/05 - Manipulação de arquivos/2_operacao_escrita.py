arquivo = open(
    "/home/joaocarlos/Documentos/Estudos/DIO/Trilha Python/05 - Manipulação de arquivos/teste.txt",
    "w",)


# arquivo.write("Sonhos são caminhos construídos pelo coração.")

# writelines() escreve uma string por vez.
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])


arquivo.close()
