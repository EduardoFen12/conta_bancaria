# ====================================================================================================


def lista_correntistas(dict, e=False):

    correntistas = []

    if e:

        emails = []
        
        for correntista in dict:

            correntistas.append(correntista)
            emails.append(dict[correntista]["Email"])

        return correntistas, emails

    for correntista in dict:

        correntistas.append(correntista)

    return correntistas


def autentifica_dados(dict):

    correntistas, emails = lista_correntistas(dict, e=True)

    nome = input("\nInforme o nome do correntista: ")

    while nome in correntistas:

        nome = input(f"\n O correntista {nome} já está cadastrado! Informe outro nome: ")

    email = input("\nInforme o email do correntista: ")

    while email in emails:

        email = input(f"\n O email {email} já está em uso! Informe outro email: ")

    saldo = float(input("\nInforme o saldo do correntista: "))

    while saldo < 0:

        saldo = float(input("\nSaldo inválido! Informe um valor maior ou igual a zero: "))

    limite = float(input("\nInforme o limite da conta: "))

    while limite < 0:

        limite = float(input("\nLimite inválido! Informe um valor maior ou igual a zero: "))

    return nome, email, saldo, limite
    

def criar_conta(dict):

    nome, email, saldo, limite = autentifica_dados(dict)

    dados = {}
    dados["Saldo"] = saldo
    dados["Email"] = email
    dados["Limite"] = limite

    dict[nome] = dados


def buscar(dict):

    correntistas = lista_correntistas(dict)

    nome = input("\nInforme o nome do correntista: ")

    while nome not in correntistas:

        nome = input(f"\n O correntista {nome} não está cadastrado! Informe outro nome: ")

    print(f'''
    Correntista: {nome}
    Email:       {dict[nome]["Email"]}
    Saldo:       {dict[nome]["Saldo"]}
    Limite:      {dict[nome]["Limite"]}
    ''')


def modificar_limite(dict, correntista):

    print(f"\nO limite atual de {correntista} é R${dict[correntista]['Limite']:.2f}")

    novo_limite = float(input("\nInforme o novo limite dessa conta: "))

    while novo_limite < 0:

        novo_limite = float(input("\nLimite inválido! Informe um valor maior ou igual a zero: "))

    dict[correntista]["Limite"] = novo_limite

    if dict[correntista]["Limite"] == novo_limite:

        print(f"\nO novo limite de {correntista} é R${novo_limite:.2f}")


def saque(dict, correntista):

    saque_max = dict[correntista]['Saldo'] + dict[correntista]['Limite']

    print(f"\nO saldo atual de {correntista} é R${dict[correntista]['Saldo']:.2f}, portanto o saque máximo é de {saque_max:.2f}")

    saque = float(input("\nInforme o valor do saque: "))

    while saque > saque_max:

        saque = float(input(f"\nValor do saque excede o limite da conta! \nInforme um valor inferior ou igual a {saque_max:.2f}: "))

    dict[correntista]['Saldo'] -= saque

    print(f"\nO saldo atual de {correntista} é {dict[correntista]['Saldo']:.2f}")


def deposito(dict, correntista):

    print(f"\nO saldo atual de {correntista} é R${dict[correntista]['Saldo']:.2f}")

    deposito = float(input("\nInforme o valor do deposito: "))

    while deposito <= 0:

        deposito = float(input(f"\nO valor de deposito não pode ser menor ou igual a zero! \nInforme outro valor: "))
    
    dict[correntista]['Saldo'] += deposito

    print(f"\nO saldo atual de {correntista} é {dict[correntista]['Saldo']:.2f}")


def excluir(dict, nome):

    correntistas = lista_correntistas(dict)

    nome = input("Informe o nome do dono da conta: ")

    while nome not in correntistas:

        nome = input(f"\n O correntista {nome} não está cadastrado! Informe outro nome: ")

    resposta = input(f"Tem certeza que deseja excluir a conta do correntista {nome}? \nDigite '1' para confirmar e qualquer outro caracter para cancelar a operção e voltar para o menu: ")
    
    if resposta == "1":

        dict.pop(nome)

    if nome not in dict:

        print(f"\nConta do correntista {nome} excluida com sucesso!")

    