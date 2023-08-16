
# ====================================================================================================

from f_arquivo import *
from f_gerenciamento_conta import *

# ====================================================================================================


# FUNÇÕES:


def menu():

    resposta = ' '

    while resposta not in [1, 2, 3, 4, 99]:

        resposta = int(input('''
             ====================================
            |                                    |
            |          CONTAS BANCÁRIAS          |
            |                                    |
            | 1. Criar nova conta                |
            | 2. Buscar por uma conta            |
            | 3. Atualizar os dados              |
            | 4. Remover uma conta               |
            |                                    |
            | 99. SAIR                           |
            |                                    |
             ====================================

             Digite a opção desejada: '''))

        return resposta

def menu_atualizar():

    resposta = ' '

    while resposta not in [1, 2, 3, 99]:

        resposta = int(input('''
             ====================================
            |                                    |
            |          ATUALIZAR  DADOS          |
            |                                    |
            | 1. Modificar limite da conta       |
            | 2. Saque                           |
            | 3. Deposito                        |
            |                                    |
            | 99. SAIR                           |
            |                                    |
             ====================================

             Digite a opção desejada: '''))

        return resposta


# ====================================================================================================


# VARIÁVEIS E CONSTANTES:


src_bd = "conta_bancaria/bd.json"

dicionario = monta_dict(src_bd)

resposta_menu = menu()


# ====================================================================================================


# PROGRAMA PRINCIPAL:


while resposta_menu != 99:

    match resposta_menu:
        
        case 1:

            criar_conta(dicionario)

            resposta_menu = menu()

        case 2:

            buscar(dicionario)

            resposta_menu = menu()

        case 3:
            
            correntistas = lista_correntistas(dicionario)

            nome = input("\nInforme o nome do correntista: ")

            while nome not in correntistas:

                nome = input(f"\n O correntista {nome} não está cadastrado! Informe outro nome: ")

            resposta = menu_atualizar()

            while resposta != 99:

                match resposta:

                    case 1:
                        
                        modificar_limite(dicionario, nome)

                        resposta = menu_atualizar()

                    case 2:

                        saque(dicionario, nome)

                        resposta = menu_atualizar()

                    case 3:

                        deposito(dicionario, nome)

                        resposta = menu_atualizar()

            resposta_menu = menu()

        case 4:

            excluir(dicionario)

            resposta_menu = menu()


salvar(dicionario, src_bd)


# =====================================================================