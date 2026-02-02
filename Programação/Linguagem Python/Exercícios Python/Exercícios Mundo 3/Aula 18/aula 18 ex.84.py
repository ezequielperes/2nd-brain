pessoas = []
peso_maior = peso_menor = 0
while True:
    nome = input('Informe o nome: ').capitalize()
    peso = float(input('Informe o peso: '))

    if len(pessoas) == 0:
        peso_maior = peso_menor = peso
    elif peso > peso_maior:
        peso_maior = peso
    elif peso < peso_menor:
        peso_menor = peso

    pessoas.append([nome, peso])

    while True:
        resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if resposta in 'SN':
            break
        print('Resposta inválida, tente novamente!')
    if resposta == 'N':
        break

print('-='*30)
print(f'Você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {peso_maior:.1f}Kg, Peso de', end=' ')
for pessoa in pessoas:
    if pessoa[1] == peso_maior:
        print(f'[{pessoa[0]}]', end=' ')
print(f'\nO menor peso foi de {peso_menor:.1f}Kg, Peso de', end=' ')
for pessoa in pessoas:
    if pessoa[1] == peso_menor:
        print(f'[{pessoa[0]}]', end=' ')
