menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 5000
limite = 500
numero_de_saques = 0
LIMITE_SAQUES = 3
extrato = ""

while True:
    print(menu)
    opcao = input("Escolha uma opção: ")
    
    if opcao == "q":
        print("Saindo...")
        break
    
    elif opcao == "d":
        valor = float(input("Qual o valor da quantia? "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("A operação falhou! O valor inserido é inválido")

    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))
        if numero_de_saques < LIMITE_SAQUES:
            if valor > 0 and valor<=saldo:
                saldo -= valor
                extrato += f"Saque: R${valor:.2f}\n"
                numero_de_saques += 1
            else:
                print("Não foi possível realizar a operação! Saldo insuficiente ou valor inválido.")
        else:
            print("Número máximo de saques atingido!")
            if valor>saldo:
                print("Não foi possível concluir a operação")

    elif opcao == "e":
        print("Extrato:")
        print(extrato)
        print(f"Saldo disponível: R${saldo:.2f}\n")
        
    else:
        print("Opção inválida! Escolha uma opção válida.")
