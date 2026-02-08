import moeda

preco = float(input('Digite o preço: R$'))

print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10):.2f}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13):.2f}')
print(f'O dobro de {preco} é {moeda.dobro(preco):.2f}')
print(f'A metade de {preco} é {moeda.metade(preco):.2f}')

