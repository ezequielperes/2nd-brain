while True:
    qnt_linha = int(input('Quantas linhas na matriz? '))
    qnt_coluna = int(input('Quantas colunas na matriz?'))
    if qnt_linha > 0 and qnt_coluna > 0:
        break
    print('Inválido, os valores de linha/coluna tem que ser maiores que 0 ')
matriz = [[] for _ in range(qnt_linha)]

for linha in range (qnt_linha):
    for coluna in range (qnt_coluna):
        matriz[linha].append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))
print('-='*30)
for linha in range(qnt_linha):
    for coluna in range(qnt_coluna):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()
