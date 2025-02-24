from abc import ABC, abstractmethod
from datetime import datetime
import textwrap
import random


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome_completo, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome_completo
        self.data_nascimento = data_nascimento


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "Valor": transacao.valor,
                "Tipo": transacao.__class__.__name__,
                "Data": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
            }
        )


class Conta:
    def __init__(self, cliente):
        self._saldo = 0
        # Gerando o número da conta automaticamente com 5 dígitos não repetidos
        self._numero_conta = "".join(random.sample("0123456789", 5))
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente):
        return cls(cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        saldo_excedido = valor > saldo

        if saldo_excedido:
            print("Saldo insuficiente.")

        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso.")
            return True

        else:
            print("O valor não pode ser negativo ou igual a zero.")
            return False
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("O valor não pode ser negativo ou igual a zero.")
            return False
        return True


class ContaCorrente(Conta):
    def __init__(self, cliente, limite=500, limite_saques=3):
        super().__init__(cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor_saque):
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == "Saque"
            ]
        )

        limite_excedido = valor_saque > self._limite
        saques_excedidos = numero_saques >= self._limite_saques

        if limite_excedido:
            print("Valor máximo de saque é de R$ 500,00.")

        elif saques_excedidos:
            print("Limite de saques atingido.")

        else:
            return super().sacar(valor_saque)

        return False

    def __str__(self):
        """agencia, numero_conta e cliente são os métodos property da classe Conta"""
        return f"AG.: {self.agencia}\nC.C: {self.numero_conta}\nTitular: {self.cliente.nome}"


class Transacao(ABC):
    """Uma classe abstrata com métodos abstratos"""

    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor_saque):
        self._valor_saque = valor_saque

    @property
    def valor(self):
        return self._valor_saque

    def registrar(self, conta):
        saque_ok = conta.sacar(self.valor)

        if saque_ok:
            # Adicionando esta instância no histórico
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor_deposito):
        self._valor_deposito = valor_deposito

    @property
    def valor(self):
        return self._valor_deposito

    def registrar(self, conta):
        deposito_ok = conta.depositar(self.valor)

        if deposito_ok:
            # Adicionar esta instância no histórico
            conta.historico.adicionar_transacao(self)


# -----------------# Menu # ------------------ #
def menu():
    menu = """
    Bem-vindo ao Barsan Bank!

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [ec] Exibir Contas
    [q] Sair

    => """
    # https://docs.python.org/pt-br/3.13/library/textwrap.html#textwrap.dedent
    return input(textwrap.dedent(menu))  # Dedent remove a identação do texto


def buscar_cpf(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
        return None

    # cliente = [cliente for cliente in clientes if cliente.cpf == cpf]
    # return cliente[0] if cliente else None


def recuperar_conta(cliente):
    """Usando a implementação do professor"""
    if not cliente.contas:
        print("Cliente não possui conta cadastrada.")
        return

    # FIXME: não permite cliente escolhar a conta
    return cliente.contas[0]


def depositar(clientes):
    """Implementação do professor"""
    cpf = input("Digite o número do C.P.F: ")
    cliente = buscar_cpf(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return

    valor_deposito = float(input("Digite o valor a ser depositado: "))
    transacao = Deposito(valor_deposito)

    conta = recuperar_conta(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    """Implementação do professor"""
    cpf = input("Digite o número do C.P.F.: ")
    cliente = buscar_cpf(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return

    valor_saque = float(input("Digite o valor do saque: "))
    transacao = Saque(valor_saque)

    conta = recuperar_conta(cliente)

    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def extrato(clientes):
    cpf = input("Digite o número do C.P.F.: ")
    cliente = buscar_cpf(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return

    conta = recuperar_conta(cliente)

    if not conta:
        return

    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"{transacao['Tipo']}:\nR$ {transacao['Valor']:.2f}"

    print(f"Saldo: R$ {conta.saldo:.2f}")
    print("Extrato:")
    print(extrato)


def criar_cliente(clientes):
    cpf = input("Digite o número do C.P.F.: ")
    cliente = buscar_cpf(cpf, clientes)

    if cliente:
        print("C.P.F já cadastrado.")
        return

    nome_completo = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço (logradouro, num - bairro - cidade/uf): ")
    cliente = PessoaFisica(
        cpf=cpf,
        nome_completo=nome_completo,
        data_nascimento=data_nascimento,
        endereco=endereco,
    )

    clientes.append(cliente)

    print("Cliente criado.")


def criar_conta(clientes, contas):
    cpf = input("Digite o número do C.P.F.: ")
    cliente = buscar_cpf(cpf, clientes)

    if not cliente:
        print("C.P.F não cadastrado.")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente)
    contas.append(conta)
    cliente.contas.append(conta)


def exibir_contas(contas):
    """Implementação do professor"""
    for conta in contas:
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            # num_conta = len(contas) + 1
            criar_conta(clientes, contas)
        elif opcao == "ec":
            exibir_contas(contas)
        elif opcao == "q":
            print("Obrigado por utilizar nossos serviços.")
            break
        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )

main()