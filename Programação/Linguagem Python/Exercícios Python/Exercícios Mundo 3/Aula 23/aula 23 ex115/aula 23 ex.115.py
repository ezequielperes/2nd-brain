from sistema import *
from arquivo import *

arq = 'banco-de-dados.txt'
criar_arquivo(arq)

while True:
    resposta = menu_principal(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resposta == 1:
        interface.titulo('Opção 1:', 'Ver pessoas cadastradas')
        banco_dados(arq)
    elif resposta == 2:
        interface.titulo('Opção 2:', 'Cadastrar nova pessoa')
        cadastrar(arq)
    elif resposta == 3:
        interface.titulo('Opção 3:','Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO: Digite apenas 1, 2 ou 3 !\033[m')