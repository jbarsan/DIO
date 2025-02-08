import textwrap

def menu():
    menu ="""
    Bem-vindo ao Barsan Bank!

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [eu] Exibir Usuários
    [ec] Exibir Contas
    [q] Sair

    => """
    # https://docs.python.org/pt-br/3.13/library/textwrap.html#textwrap.dedent
    return input(textwrap.dedent(menu)) # Dedent remove a identação do texto

# Definindo funções

def buscar_cpf(cpf, usuarios):
    """Função para buscar um usuário pelo CPF."""
    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            return usuario
    
    # Usando list comprehension
    # usuario = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    # return usuario[0] if usuario else None
    
    return None


def criar_usuario(usuarios):
    """Função para criar um usuário."""
    print("Para que possamos criar seu cadastro em nosso banco, precisamos de algumas informações.")
    cpf = input("Por favor, digite seu CPF (Somente os números): ")

    # Verifica se o CPF já foi cadastrado
    usuario = buscar_cpf(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado.")
        return
    
    nome_completo = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Digite seu endereço (Logradouro, número - bairro - cidade/uf): ")
    
    usuarios.append({"Nome": nome_completo, "CPF": cpf, "Data de Nascimento": data_nascimento, "Endereço": endereco})

    print(f"Usuário {nome_completo} cadastrado com sucesso.")


def criar_conta(agencia, numero_conta, usuarios, contas):
    """Função para criar uma conta e vincular a um cpf."""
    print("Para que possamos criar uma conta para você em nosso banco, precisamos de algumas informações.")
    cpf = input("CPF (somente os números): ")
    usuario = buscar_cpf(cpf, usuarios)

    if usuario:
        contas.append({"Número": numero_conta, "Agência": agencia, "CPF": cpf, "Saldo": 0})
        print(f"Conta {numero_conta}, criada com sucesso.")
    else:
        print("Usuário não encontrado.")


def depositar(saldo, valor_deposito, extrato, /):
    """Função para realizar um depósito."""
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"+ R$ {valor_deposito:.2f}\n"
        print('Depósito realizado com sucesso.')
    else:
        print("O valor não pode ser negativo ou igual a zero.")

    return saldo, extrato


def sacar(*, saldo, valor_saque, extrato, numero_saques, limite, limite_saques):
    """Função para realizar um saque."""
    # realizando verificações
    # Essa verificação é melhor do que a anterior, pois é mais fácil de entender o que está sendo verificado
    saldo_excedido = valor_saque > saldo
    limite_excedido = valor_saque > limite
    saques_excedidos = numero_saques >= limite_saques

    if saldo_excedido:
        print("Saldo insuficiente.")
    elif limite_excedido:
        print("Valor máximo de saque é R$ 500,00.")
    elif saques_excedidos:
        print("Limite de saques atingido.")
    else:
        saldo -= valor_saque
        extrato += f"- R$ {valor_saque:.2f}\n"
        numero_saques += 1
        print('Saque realizado com sucesso.\nObrigado por utilizar nossos serviços.')
    return saldo, extrato, numero_saques


def extrato_bancario(saldo, /, *, extrato):
    """Função para exibir o extrato bancário."""
    if extrato == "":
        print("Não foram realizadas movimentações.")
    else:
        print(f"Saldo: R$ {saldo:.2f}")
        print("Extrato:")
        print(extrato)


def exibir_usuarios(usuarios):
    """Função para exibir os usuários cadastrados."""
    if not usuarios:
        print("Não há usuários cadastrados.")
    else:
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(f"Nome: {usuario['Nome']} - CPF: {usuario['CPF']}")


def exibir_contas(contas):
    """Função para exibir as contas cadastradas."""
    if not contas:
        print("Não há contas cadastradas.")
    else:
        print("Contas cadastradas:")
        for conta in contas:
            print(f"Agência: {conta['Agência']} - Número: {conta['Número']} - CPF: {conta['CPF']}")


# Programa principal

def main():
    # Definindo constantes
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    # Definindo variáveis
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    contas = []
    usuarios = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito): R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor_saque=valor, extrato=extrato, numero_saques=numero_saques, limite=limite, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            extrato_bancario(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            criar_conta(AGENCIA, len(contas) + 1, usuarios, contas)

        elif opcao == "eu":
            exibir_usuarios(usuarios)

        elif opcao == "ec":
            exibir_contas(contas)

        elif opcao == "q":
            print("Obrigado por utilizar nossos serviços.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()