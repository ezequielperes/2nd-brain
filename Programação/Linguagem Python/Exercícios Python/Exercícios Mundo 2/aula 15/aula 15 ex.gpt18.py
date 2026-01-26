while True:
    resposta = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    while resposta not in 'SN':
        print('\033[31mResposta Inválida, Digite novamente!\033[m')
        resposta = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if resposta == 'N':
        break
print('Fim do programa')