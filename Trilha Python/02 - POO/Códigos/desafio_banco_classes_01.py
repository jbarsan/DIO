from abc import ABC, abstractmethod
from datetime import datetime


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
            }
        )


class Conta:
    def __init__(self, numero_conta, cliente):
        self._saldo = 0
        self._numero_conta = numero_conta
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero_conta, cliente):
        return cls(numero_conta, cliente)

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
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
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
        return f"AG.: {self.agencia}\nC.C: {self.numero_conta}\nTitular: {self.cliente}"


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
                """Adicionando esta instância no histórico"""
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
            """Adicionar esta instância no histórico"""
            conta.historico.adicionar_transacao(self)
