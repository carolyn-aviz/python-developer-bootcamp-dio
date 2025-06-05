import textwrap

def menu():
    menu = """
    Bem-vindo ao banco!
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Criar Usuário
    5 - Criar Conta
    6 - Listar Contas
    7 - Sair
    """
    return int(input(textwrap.dedent(menu)))

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"- Depósito: R$ {valor:.2f}\n"
        print(f"\n✓ Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\n✗ Valor inválido! O depósito deve ser maior que zero.")
    return saldo, extrato

def sacar(*, saldo, valor, limite, numero_saques, limite_saques, extrato):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n✗ Operação falhou! Saldo insuficiente.")
    elif excedeu_limite:
        print(f"\n✗ Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
    elif excedeu_saques:
        print("\n✗ Operação falhou! Número máximo de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"- Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\n✓ Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\n✗ Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n══════════════ EXTRATO ══════════════")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("═════════════════════════════════════")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF do usuário (somente números): ")
    usuario_existente = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)

    if usuario_existente:
        print("\n✗ Já existe um usuário cadastrado com este CPF!")
    else:
        nome = input("Digite o nome completo: ")
        data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
        endereco = input("Digite o endereço (logradouro, nº - bairro - cidade/UF): ")
        usuarios.append({'nome': nome, 'cpf': cpf, 'data_nascimento': data_nascimento, 'endereco': endereco})
        print("\n✓ Usuário cadastrado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário (somente números): ")
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)

    if not usuario:
        print("\n✗ Usuário não encontrado. Cadastre o usuário primeiro!")
        return None

    conta = {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print(f"\n✓ Conta criada com sucesso! Número: {numero_conta}")
    return conta

def listar_contas(contas):
    if not contas:
        print("\n✗ Nenhuma conta cadastrada no sistema.")
        return

    print("\n════════════ CONTAS CADASTRADAS ════════════")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(textwrap.dedent(linha))
        print("════════════════════════════════════════════")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                extrato=extrato,
            )

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 7:
            print("\n✓ Obrigado por usar nosso sistema! Até logo!")
            break

        else:
            print("\n✗ Opção inválida! Por favor, selecione uma opção válida.")

if __name__ == "__main__":
    main()