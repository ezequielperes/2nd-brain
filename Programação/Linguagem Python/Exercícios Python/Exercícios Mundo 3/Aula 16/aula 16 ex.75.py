numeros = (
    int(input('Digite um valor: ')),
    int(input('Digite outro valor: ')),
    int(input('Digite mais um valor: ')),
    int(input('Digite o último valor: '))
    )
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O valor 3 apareceu:',end= ' ')
    for c, n in enumerate(numeros):
        if n == 3:
            print(f'{c+1}ª Posição', end=' ')
else:
    print('O valor 3 não foi digitado')

print(f'\nOs valores pares digitados foram:', end= ' ')
validacao_par = 0
for c, n in enumerate(numeros):
    if n % 2 == 0:
        print(numeros[c], end=' ')
        validacao_par += 1
if validacao_par == 0:
    print('Nenhum')