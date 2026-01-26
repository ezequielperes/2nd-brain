maior = menor = media = c = 0
opcao = ' '
while opcao not in 'N':
    valor = int(input('Digite um valor: '))
    media += valor
    c += 1
    if c == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    opcao = input('Deseja continuar? [S/N] ').strip().upper()
    while opcao not in 'SN':
        opcao = input('\033[31mTente Novamente!\033[m'
                      '\nDeseja continuar? [S/N]').strip().upper()
media /= c
print(f'A média dos {c} números digitados foi de: {media:.2f}'
      f'\nO maior número digitado foi: {maior}'
      f'\nO menor número digitado foi: {menor}')
