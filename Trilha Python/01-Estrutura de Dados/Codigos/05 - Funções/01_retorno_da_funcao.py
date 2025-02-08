def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


# print(calcular_total([10, 20, 34]))  # 64
# print(retorna_antecessor_e_sucessor(10))  # (9, 11)

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro {marca} {modelo} {ano} {placa} salvo com sucesso!")

# salvar_carro("Fiat", "Uno", 2020, "ABC-1234")  # Carro Fiat Uno 2020 ABC-1234 salvo com sucesso!

# Passando argumento como diciionário
# salvar_carro(**{"marca": "Ford", "modelo": "Pampa", "ano": 1986, "placa": "adf-1234"})  # Carro Fiat Uno 2020 ABC-1234 salvo com sucesso!

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Sábado, 08 de fevereiro de 2025", "Zen do Python", "Lindo é melhor que feio", "Explícito é melhor que implícito", "Simples é melhor que complexo", "Complexo é melhor que complicado", "Plano é melhor que aninhado", "Esparso é melhor que denso", "Legibilidade conta", "Os casos especiais não são especiais o bastante para quebrar as regras", "Embora a praticidade vença a pureza", "Erros nunca devem passar silenciosamente", "A menos que sejam explicitamente silenciados", "Diante da ambiguidade, recuse a tentação de adivinhar", "Deveria haver um - e preferencialmente só um - modo óbvio para fazer algo", "Embora esse modo possa não ser óbvio a princípio a menos que você seja holandês", "Agora é melhor que nunca", "Embora nunca frequentemente seja melhor que já", "Se a implementação é difícil de explicar, é uma má ideia", "Se a implementação é fácil de explicar, pode ser uma boa ideia", "Namespaces são uma grande ideia - vamos ter mais dessas!", autor="Tim Peters", ano=1999)

