from random import randint
from emoji import emojize
from time import sleep
jogador = {}
jogadores = []
print('Valores sorteados:')
for c in range(4):
    jogador['n_jogador'] = f'Jogador {c+1}'
    jogador['dado'] = randint(1, 6)
    print(emojize(f'{jogador["n_jogador"]} -> :game_die: {jogador["dado"]} :game_die:'))
    jogadores.append(jogador.copy())
    sleep(0.75)

print(f'{"< RANKING DOS JOGADORES >":-^30}')
ranking = sorted(jogadores, key=lambda x: x['dado'], reverse=True)
for c, jogador in enumerate(ranking):
    sleep(0.75)
    print(emojize(f'{c+1}º Lugar -> {jogador["n_jogador"]} -> :game_die: {jogador["dado"]} :game_die:'))
print('-'*30)