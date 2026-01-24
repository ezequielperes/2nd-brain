from random import randint
from time import sleep

print('\033[1;33m-'*50)
sleep(0.5)
print(f'{"\033[1;31mDESCUBRA O NÚMERO\033[m":^60}')
sleep(0.5)
print('\033[1;33m-'*50)
pc = randint(0, 10)
player = -1
cont = -1

sleep(0.75)
print('\033[37mObjetivo: descubra o número que seu adiversário pensou!')
sleep(1)
print('LISTEN! é um número de 0 a 10!')
sleep(1)
while pc != player:
    sleep(1)
    player = int(input('\033[35mADIVINHE O NÚMERO QUE EU PENSEI!!!'))
    sleep(1)
    if player > 10 or player < 0:
        player = 0
        print('\033[1;31mEntrada Invalida!')
    cont += 1
    if player - 1 == pc or player + 1 == pc:
        print('\033[1;31mTA QUENTE!!! TÁ PEGANDO FOGOOO!!!')
    elif player > pc or player < pc:
        print('\033[1;34m Ainn tá friozinhummm... Você erroummm')
sleep(1)
if cont == 0:
    print('\033[32mO QUE?!?!?! IMPOSSÍVEL, VOCÊ ACERTOU DE PRIMEIRA?!?!?!? NAUMMMMMMMMM!!!!!!!!')
elif cont >= 5:
    print(f'\033[33mIHHH VOCÊ É RUINZINHO EM, ERROU {cont}...')
    sleep(1)
    print('\033[1;31mQUE VERGONHA MUAAHHAHAHAHA!!!')
else:
    print(f'Chato(a), você acertou... você errou {cont} vezes!')