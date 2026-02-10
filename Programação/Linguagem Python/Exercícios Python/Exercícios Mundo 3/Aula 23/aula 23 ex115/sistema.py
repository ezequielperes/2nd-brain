import interface
import ast
from time import sleep
def menu_principal(lista):
    while True:
        interface.titulo('MENU PRINCIPAL')
        for c, item in enumerate(lista):
            print(f'\033[33m{c+1} - \033[34m{lista[c]}\033[m')
            sleep(0.25)
        interface.linha()
        while True:
            try:
                resposta = int(input('\033[33mSua Opção: \033[m'))
                break
            except (ValueError, TypeError):
                print('\033[31mERRO: Digite um número inteiro !\033[m')
            except KeyboardInterrupt:
                print('\033[33mERRO: Digite 1, 2 ou 3 !')
        return resposta


def banco_dados(arq):
    try:
        arquivo = open(arq, 'rt')
    except FileNotFoundError:
        print('\033[31mErro ao ler o arquivo!\033[m')
    for dado in arquivo.readlines():
        dado = ast.literal_eval(dado)
        print(f'{dado["nome"]:30} {dado["idade"]:>4}')
    arquivo.close()



def cadastrar(arq=None):
    cadastro = {}
    try:
        arquivo = open(arq, 'at')
    except FileNotFoundError:
        print('\033[31mErro ao abrir o arquivo!\033[m')

    while True:
        cadastro['nome'] = input('Nome: ').strip().title()
        if cadastro['nome'].replace(' ', '').isalpha():
            break
        print('\033[31mERRO: Digite apenas letras do alfabeto!\033[m')
    while True:
        try:
            cadastro['idade'] = int(input('Idade: '))
            break
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[31mERRO: Digite apenas idades válidas!\033[m')
    arquivo.write(f'{cadastro}\n')
    print(f'\033[32mSucesso! Novo registro de {cadastro["nome"]}!\033[m')
    arquivo.close()
    return cadastro
