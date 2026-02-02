numeros = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite {c+1}º valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('-='*30)
numeros[0].sort()
numeros[1].sort()
print(f'Pares: {numeros[0]}')
print(f'Impares: {numeros[1]}')
