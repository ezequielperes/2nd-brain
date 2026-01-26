from random import randint
from time import sleep
print('-'*30)
print('JOGO DE ADIVINHAÇÃO'.center(30))
print('-'*30)
print('\033[1;37mObjetivo: Tentar adivinhar o número que o computador pensou.\033[m')
pc = randint(0, 10)
player = -1
c = 0
while player != pc:
    player = int(input('Digite um palpite:'))

    if 0 > player or player > 10:
        print('\033[1;31mEntrada Inválida!\033[m')
    else:
        if player != pc:
            print('\033[1;31mERROU!\033[m Tente novamente mais um palpite')
            c += 1

if c == 1:
    print('PARABÉNS VOCÊ ACERTOU DE PRIMEIRA!')
else:
    print(f'Parabéns você acertou e você fez {c} palpites errados!')