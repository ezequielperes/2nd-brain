from time import sleep
from random import randint
print('-='*20)
print('IMPAR OU PAR!!!'.center(40))
print('-='*20)
print('\033[37mObjetivo: ganhar o máximo de vezes do adiversário!'
      '\nBoa sorte!\033[m')
sleep(1)
ganhou = 0
while True:
    p1 = int(input('Escolha um número de 0 a 10!'))
    while p1 < 0 or p1 > 10 :
        print('\033[31mEntrada inválida! Tente novamente!\033[m')
        p1 = int(input('Escolha um número de 0 a 10!'))
    sleep(0.5)
    print('[1] Impar')
    print('[2] Par')
    escolha_p1 = int(input('Escolha:'))
    while escolha_p1 < 1 or escolha_p1 > 2:
        print('\033[31mEntrada Inválida! Tente novamente!\033[m')
        print('[1] Impar')
        print('[2] Par')
        escolha_p1 = int(input('Escolha: '))
    sleep(1)
    pc = randint(0, 10)
    soma = p1 + pc
    print('\033[35mIMPAR')
    sleep(0.5)
    print('OU')
    sleep(0.25)
    print('PAR!!!\033[m')
    sleep(1)
    if (soma % 2 == 0 and escolha_p1 == 2) or (soma % 2 != 0 and escolha_p1 == 1):
        print('\033[1;32mVOCÊ GANHOU!!!\033[m!')
        sleep(0.5)
        print(f'meu número foi {pc} e o seu foi {p1}... {pc} + {p1} = {soma}')
        sleep(0.5)
        if escolha_p1 == 1:
            print('\033[32mEste número é IMPAR!!!')
        else:
            print('\033[32mEste número é PAR!!!')
        sleep(0.5)
        print('PARABÉNS!!!\033[m')
        sleep(1)
        ganhou += 1
    else:
        print('\033[1;31mVOCÊ PERDEU!!!!\033[m')
        sleep(0.5)
        print(f'meu número foi {pc} e o seu foi {p1}... {pc} + {p1} = {soma}')
        sleep(0.5)
        if escolha_p1 == 2:
            print('\033[31mEste número é IMPAR!!! EU VENCIII!!!!\033[m')
        else:
            print('\033[31mEste número é PAR!!! EU VENCIII!!!!\033[m')
        break
    print('-'*20)
sleep(1)
print(f'Você ganhou {ganhou} vezes!')
sleep(0.5)
if ganhou <= 2:
    print('\033[31mVocê é meio ruizinho em! Mais sorte na próxima!\033[m')
elif ganhou < 5:
    print('\033[33mNada Mal... Vamos ver na próxima!\033[m')
else:
    print('\033[32mUauuu muito bem! onde você aprendeu a jogar tão bem assim?\033[m')
