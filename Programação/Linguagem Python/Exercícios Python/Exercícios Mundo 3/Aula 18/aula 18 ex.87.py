while True:
    qnt_linha = int(input('Quantas linhas da matriz? '))
    qnt_coluna = int(input('Quantas colunas da matriz? '))
    if qnt_linha > 0 and qnt_coluna > 0:
        break
    print('Inválido, os valores de linha/coluna tem que ser maiores que 0')

matriz = [[] for _ in range(qnt_linha)]
soma_pares = soma_coluna3 = 0
for linha in range(qnt_linha):
    for coluna in range(qnt_coluna):
        n_matriz = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if n_matriz % 2 == 0:
            soma_pares += n_matriz
        if coluna == 2:
            soma_coluna3 += n_matriz
        matriz[linha].append(n_matriz)

print('-='*30)
for linha in range(qnt_linha):
    for coluna in range(qnt_coluna):
        print(f'[{matriz[linha][coluna]:^5}]', end= ' ')
    print()
print('-='*30)
print(f'A soma dos valores pares é {soma_pares}')
if qnt_coluna >= 3:
    print(f'A soma dos valores na terceira coluna é {soma_coluna3}')
if qnt_linha >= 2:
    print(f'O maior valor da segunda linha é {max(matriz[1])}')
