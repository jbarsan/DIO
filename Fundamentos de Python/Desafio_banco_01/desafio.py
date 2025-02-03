menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Valor do depósito: "))

        # Verifica se valor é negativo ou igual a zero e não permite a operação
        if valor > 0:
            saldo += valor
            extrato += f"+ R$ {valor:.2f}\n"            
        else:
            print("O valor não pode ser negativo ou igual a zero.")            

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Valor do saque: "))
            if valor <= limite:
                if valor > 0:
                    if saldo >= valor:
                        saldo -= valor
                        extrato += f"- R$ {valor:.2f}\n"
                        numero_saques += 1
                    else:
                        print("Saldo insuficiente.")
                else:
                    print("O valor não pode ser negativo ou igual a zero.")            
            else:
                print("Valor máximo de saque é R$ 500,00.")
        else:
            print("Limite de saques atingido.")

    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(f"Saldo: R$ {saldo:.2f}")
            print("Extrato:")
            print(extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
