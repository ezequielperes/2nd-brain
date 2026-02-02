from random import randint
from time import sleep
print('-'*40)
print('Jogo da Mega Cena'.center(40))
print('-'*40)

qnt_jogos = int(input('Quantos jogos você quer sortear? '))
print(f'{f" Sorteando {qnt_jogos} jogos ":-^40}')
for c in range(qnt_jogos):
    jogos = []
    while True:
        n = randint(1, 60)
        if n not in jogos:
            jogos.append(n)
        if len(jogos) == 6:
            break
    jogos.sort()
    print(f'Jogo {c+1}: {jogos}')
    sleep(0.75)
print(f'{" < Boa Sorte > ":-^40}')


