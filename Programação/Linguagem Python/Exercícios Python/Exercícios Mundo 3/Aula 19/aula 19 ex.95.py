jogadores = []
while True:
    jogador = {
        'nome': input('Nome: ').title().strip(),
        'gols': [],
        'total_gols': 0
    }
    qnt_partidas = int(input(f'quantas partidas {jogador["nome"]} jogou: '))
    for c in range(qnt_partidas):
        jogador['gols'].append(int(input(f'Gols na {c+1} partida: ')))
    jogador['total_gols'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    while True:
        resposta = input('Quer continuar? [S/N] ').upper().strip()[0]
        if resposta in 'SN':
            break
        print('Inválido, tente novamente !')
    if resposta == 'N':
        break
    print('-'*30)
print('-='*30)

print(f'Nº Nome {'Gols':^30} Total')
print('-'*60)
for c, jogador in enumerate(jogadores):
    print(c, f' {jogador["nome"]:<18} {str(jogador["gols"]):<20}{jogador["total_gols"]}')
print('-'*60)

while True:
    n_jogador = int(input('Mostrar dados de qual jogador (999 para parar) ? [Nº] '))
    if n_jogador == 999:
        break
    if 0 <= n_jogador <= len(jogadores)-1:
      print(f'-- Levantamento do jogador {jogadores[n_jogador]["nome"]}:')
      for c, qnt_gols in enumerate(jogadores[n_jogador]['gols']):
          print(f' No jogo {c+1} fez {qnt_gols} gols')
    else:
        print(f'Inválido, não existe um jogador com o Nº{n_jogador}. Tente novamente !')
    print('-'*30)
print('Finalizando o programa...')
