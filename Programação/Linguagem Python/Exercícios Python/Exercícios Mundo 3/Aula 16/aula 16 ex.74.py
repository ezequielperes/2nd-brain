from random import randint

n_aleatorios = (randint(0,10),
                randint(0,10),
                randint(0,10),
                randint(0,10),
                randint(0,10)
                )

maior = menor = n_aleatorios[0]
print(f'Os números sortidos foram:', end= ' ')
for n in n_aleatorios:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    print(n, end= ' ')


print(f'\nO maior número foi: {maior}')
print(f'O menor número foi: {menor}')