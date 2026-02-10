from time import sleep

def encontrar_arquivo(arq):
    try:
        arq = open(arq, 'rt')
        arq.close()
        return True
    except FileNotFoundError:
        return False


def criar_arquivo(arq):
    if not encontrar_arquivo(arq):
        print(f'\033[31m {arq} não exite!\033[m')
        sleep(0.5)
        print('\033[33mCriando...\033[m')
        arq = open(arq, 'wt+')
        arq.close()
        sleep(1)
        print('\033[32mArquivo criado com sucesso!\033[m')
    else:
        print('\033[32mO arquivo já existe!\033[m')

