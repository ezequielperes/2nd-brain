resposta = 'S'
while resposta == 'S':
    print('Continuando...')
    resposta = (input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while resposta not in 'SN':
        print('\033[31mResposta inválida! Digite Novamente!\033[m')
        resposta = input('Deseja continuar? [S/N]: ').strip().upper()[0]
print('Programa encerrado')