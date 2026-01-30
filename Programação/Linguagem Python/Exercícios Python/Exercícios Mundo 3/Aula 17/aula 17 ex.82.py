#o jeito mais fácil:
valores = list()
valores_pares = list()
valores_impares = list()
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)
    while True:
        resposta = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if resposta in 'SN':
            break
        print('Resposta inválida, tente novamente!')
    if resposta in 'N':
        break
print('A lista total foi:')
print(valores)
print('A lista de pares foi:')
print(valores_pares)
print('A lista de impares foi:')
print(valores_impares)

#or

#Jeito mais difícil (o que o professor pediu) ;-;

valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    while True:
        resposta = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if resposta in 'SN':
            break
        print('Resposta inválida, tente novamente!')
    if resposta in 'N':
        break
valores_pares = list()
valores_impares = list()
for valor in valores:
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)
print('A lista total foi:')
print(valores)

print('A lista de pares foi:')
print(valores_pares)

print('A lista de ímpares foi:')
print(valores_impares)
