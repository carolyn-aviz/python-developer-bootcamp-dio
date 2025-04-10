# Criação de variáveis


menu = ("""
          Bem-vindo ao banco!
          1 - Depositar
          2 - Sacar
          3 - Extrato
          4 - Sair
          """)
saldo = 0
limite = 500
numero_saques = 3
saques_realizados = 0
extrato = ""
saque = 0
 
while True:


    opcao = int(input(menu))


    if opcao == 1:
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"- Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Valor inválido! O depósito deve ser maior que zero.")
    elif opcao == 2:
        if saques_realizados >= numero_saques:
            print("Número máximo de saques atingido!")
            continue
           
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque > limite:
            print(f"Valor inválido! O saque não pode ser maior que R$ {limite:.2f}.")
        elif saques_realizados >= numero_saques:
            print("Número máximo de saques atingido!")
        elif valor_saque > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= valor_saque
            saques_realizados += 1
            extrato += f"- Saque: R$ {valor_saque:.2f}\n"
    elif opcao == 3:
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print("Movimentações:")
            print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == 4:
        print("Obrigado por usar nosso sistema! Até logo!")
        break
