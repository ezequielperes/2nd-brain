def jgdr(jogador='<Desconhecido>',gols=0):
    print('-'*30)
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato.'


nome_jogador = input('Qual o nome do jogador? ')
qnt_gols = str(input('Quantos gols na partida? '))
if qnt_gols.isnumeric():
    qnt_gols = int(qnt_gols)
else:
    qnt_gols = 0
if nome_jogador.strip() == '':
    print(jgdr(gols=qnt_gols))
else:
    print(jgdr(nome_jogador, qnt_gols))