"""
Desafio

Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente está em um formato correto. Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. Desenvolva uma função programa que valide se um número de telefone tem o formato correto.

Formato esperado:
O formato aceito para números de telefone é: (XX) 9XXXX-XXXX, onde X representa um dígito de 0 a 9. Lembre-se de respeitar os espaços entre os números quando preciso.

Entrada
Uma string representando o número de telefone.

Saída
Uma mensagem indicando se o número de telefone é válido ou inválido.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.
Entrada             Saída
(88) 98888-8888     Número de telefone válido.
(11)91111-1111      Número de telefone inválido.
225555-555      	Número de telefone inválido.
"""

import re


# def validar_telefone(numero: str) -> str:
#     padrao = re.compile(r"^\(\d{2}\) 9\d{4}-\d{4}$")
#     if padrao.match(numero):
#         return "Número de telefone válido."
#     return "Número de telefone inválido."


# # Testes
# numeros_teste = [
#     "(88) 98888-8888",  # Válido
#     "(11)91111-1111",  # Inválido (sem espaço após DDD)
#     "225555-555",  # Inválido (sem DDD e formato errado)
#     "(99) 91234-5678",  # Válido
#     "(01) 90000-0000",  # Válido
#     "(123) 99999-9999",  # Inválido (DDD com 3 dígitos)
#     "(11) 81111-1111",  # Inválido (não começa com 9)
# ]

# for numero in numeros_teste:
#     print(f"Entrada: {numero} -> Saída: {validar_telefone(numero)}")


def validate_numero_telefone(phone_number):
    pattern = re.compile(r"^\(\d{2}\) 9\d{4}-\d{4}$")
    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    return "Número de telefone inválido."

phone_number = input()  

result = validate_numero_telefone(phone_number)
# Imprime o resultado:
print(result)