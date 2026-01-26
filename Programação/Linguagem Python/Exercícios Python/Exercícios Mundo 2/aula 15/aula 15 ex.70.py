print('-'*20)
print('LOJA DO SERJÃO'.center(20))
print('-'*20)

total_compra = c = produto_mais_barato = produtos_mais_mil = 0

nome_mais_barato = ''
while True:
    produto = input('Nome do Produto: ').strip().capitalize()
    valor = float(input('Preço: R$'))

    c += 1
    total_compra += valor
    if valor > 1000:
        produtos_mais_mil += 1
    if c == 1 or valor < produto_mais_barato:
        produto_mais_barato = valor
        nome_mais_barato = produto

    resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while resposta not in 'SN':
        print('\033[31mEntrada Inválida, tente novamente!\033[m')
        resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break
    print('-'*20)
print('='*40)
print(f'O total gasto na compra foi de R${total_compra:.2f} e você comprou {c} produtos!'
      f'\n{produtos_mais_mil} produtos foram mais de R$1000,00 !'
      f'\nO produto mais barato foi {nome_mais_barato}, que custa R$ {produto_mais_barato:.2f} !')
