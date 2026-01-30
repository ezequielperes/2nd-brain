from random import choice
from time import sleep

print('-='*20)
print('Times Brasileirão'.center(40))
print('-='*20)
times_brasileirao = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
                     'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
                     'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
                     'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

colors = ('\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m')
for c , times in enumerate(times_brasileirao):
    if c == len(times_brasileirao) - 1:
        print(times, end='\033[m')

    else:
        print(choice(colors), times, end=' -> ')
    if c == 10:
        print('\n', times, end= ' ->')
    sleep(0.3)

print('\n','-='*20)
print('5 primeiros colocados'.center(40))
print('-='*20)
print('\n',times_brasileirao[:5],'\n')
sleep(3)

print('-='*20)
print('4 últimos colocados'.center(40))
print('-='*20)
print('\n',times_brasileirao[-4:],'\n')
sleep(3)

print('-='*20)
print('Times em ordem Alfabética'.center(40))
print('-='*20)
print('\n',sorted(times_brasileirao),'\n')
sleep(3)

print('-='*20)
print(f'O Chapecoense está na {times_brasileirao.index("Chapecoense")+1}° colocação!'.center(40))
print('-='*20)