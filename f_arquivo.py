
# ====================================================================================================

import json

# ====================================================================================================


def monta_dict(src_arquivo):

    dicionario = {}

    try: 

        with open(src_arquivo, 'r') as arquivo:

            dicionario = json.load(arquivo)

    except OSError:

        print("\nErro ao ler arquivo!")

    return dicionario

def salvar(dicionario, src_arquivo):

    try: 

        with open(src_arquivo, 'w') as arquivo:

            json.dump(dicionario, arquivo, indent=6)

        print("\nDados salvos com sucesso!")

    except OSError:

        print("\nErro ao salvar os dados!")