saldo = 500
limite_saque = 500
numero_de_saques = 0
movimentos = []

while True:
    print("Selecione uma opção:")
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = int(input())

    if opcao == 1:
        valor = float(input("Valor para saque: "))

        if valor > saldo + limite_saque:
            print("Saldo insuficiente")
        elif numero_de_saques >= 3:
            print("Limite de saques diários atingido")
        else:
            saldo -= valor
            numero_de_saques += 1
            movimentos.append(f"Saque de R${valor:.2f}")

    elif opcao == 2:    
        valor = float(input("Valor para deposito: "))

        saldo += valor
        movimentos.append(f"Deposito de R${valor}")

    elif opcao == 3:
        print("Extrato:")
        for movimento in movimentos:
            print(movimento)
        print(f"Seu saldo e R$ {saldo:.2f}")
    elif opcao == 4:
        break