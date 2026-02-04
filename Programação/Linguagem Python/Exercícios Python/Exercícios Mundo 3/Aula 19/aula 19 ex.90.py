alunos = []
while True:
    dados = dict()
    dados['nome'] = input('Nome: ').title().strip()
    while True:
        dados['média'] = float(input(f'Média de {dados["nome"]}: '))
        if 0 <= dados['média'] <= 10:
            break
        print('\033[31mInválido, apenas médias de 0 a 10 !\033[m')
    if dados['média'] < 5:
        dados['situação'] = '\033[31mReprovado\033[m'
    elif 5 <= dados['média'] < 7:
        dados['situação'] = '\033[33mRecuperação\033[m'
    else:
        dados['situação'] = '\033[32mAprovado\033[m'
    alunos.append(dados.copy())
    while True:
        resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resposta in 'SN':
            break
        print('\033[31mInválido, tente novamente!\033[m')
    if resposta == 'N':
        break
    print('-'*30)
print(f'Nome {"Média":^30} Situação')
print('-'*50)
for aluno in alunos:
    print(f'{aluno["nome"]:<16} {aluno["média"]:<18.2f} {aluno["situação"]}')
print('-'*50)