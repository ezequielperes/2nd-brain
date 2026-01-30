listagem = (
    'Lápis', 1.75,
    'Borracha', 2,
    'Caderno', 15.9,
    'Estojo', 25,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)
print('-'*50)
print('Listagem de Preços'.center(50))
print('-'*50)

for nome, valor in zip(listagem[::2], listagem[1::2]):
    print(f'{nome:.<40}R$ {valor:>7.2f}')

print('-'*50)