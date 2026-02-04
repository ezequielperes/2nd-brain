jogador = {
    'nome': input('Nome do jogador: ').capitalize(),
    'gols': [],
    'total_gols': 0
}
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
print('-'*30)
for c in range(partidas):
    jogador['gols'].append(int(input(f'Gols da {c+1}ª partida: ')))

jogador['total_gols'] = sum(jogador['gols'])
print('-'*30)
print(jogador)
print('-='*15)
for k, v in jogador.items():
    print(f'{k.title().replace("_", " ")}: {v}')
print('-='*15)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c, v in enumerate(jogador['gols']):
    print(f'=> Na {c+1}ª partida, fez {v} gols.')
print(f'Foi um total de {jogador["total_gols"]} gols')
