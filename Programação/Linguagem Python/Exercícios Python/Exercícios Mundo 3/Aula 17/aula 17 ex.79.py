valores = list()
while True:
    valor = (int(input('Digite um valor: ')))
    if valor in valores:
        print('Este valor já foi, ele não será adicionado na lista!')
    else:
        valores.append(valor)
    while True:
        resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if resposta in 'SN':
            break
        print('Resposta inválida, digite novamente!')
    if resposta == 'N':
        break
valores.sort()
print(f'Os valores digitados foram: {valores}')



