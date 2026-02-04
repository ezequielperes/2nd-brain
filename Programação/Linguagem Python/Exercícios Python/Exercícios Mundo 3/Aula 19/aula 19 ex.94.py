pessoas = []
while True:
    dados = {
        'nome': input('Nome: ').capitalize(),
        'idade': 0
    }
    while True:
        dados['sexo'] = input('Sexo [M/F]: ').upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
        print('inválido, digite apenas M ou F !')
    while True:
        dados['idade'] = int(input('Idade: '))
        if dados['idade'] > 0:
            break
        print('Inválido, Apenas valores maiores que 0 !')
    pessoas.append(dados.copy())
    while True:
        resposta = input('Deseja continuar? [S/N]').strip().upper()[0]
        if resposta in 'SN':
            break
        print('Resposta inválida, digite apenas S ou N !')
    if resposta == 'N':
        break
print(f'- O grupo tem {len(pessoas)} pessoas que foram cadastradas')

total = 0
for pessoa in pessoas:
    total += pessoa['idade']
media = total / len(pessoas)
print(f'- A média de idade do grupo é: {media:.2f} anos ')

mulheres = [p for p in pessoas if p['sexo'] == 'F']
if mulheres:
    print('- As mulheres do grupo são: ', end='')
    for pessoa in mulheres:
            print(f'[{pessoa["nome"]}]', end = ' ')
    print()
else:
    print('- Não há mulheres no grupo')

print('- As pessoas com idade acima da média são: ')
idade_decrescente = sorted(pessoas, key=lambda idade: idade['idade'], reverse=True)
for c, pessoa in enumerate(idade_decrescente):
    if pessoa['idade'] > media:
        print(f'\n{c+1}º lugar: ',end = ' ')
        for k, v in pessoa.items():
            print(f'{k.capitalize()} = {v};',end= ' ')
        print()