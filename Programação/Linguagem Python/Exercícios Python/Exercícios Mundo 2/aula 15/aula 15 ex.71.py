print('='*20)
print('BANCO LQ'.center(20))
print('='*20)
valor = int(input('Digite um valor a ser sacado: '))
i = valor
cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = 0
while True:
        if i // 50 != 0:
            cedulas_50 = i // 50
            i -= cedulas_50 * 50
        elif i // 20 != 0:
            cedulas_20 = i // 20
            i -= cedulas_20 * 20
        elif i // 10 != 0:
            cedulas_10 = i // 10
            i -= cedulas_10 * 10
        elif i // 1 != 0:
            cedulas_1 = i // 1
            i -= cedulas_1
        else:
            break
print('='*20)
print(f'Total de {cedulas_50} cédula(s) de R$50,00'
      f'\nTotal de {cedulas_20} cédulas(s) de R$20,00'
      f'\nTotal de {cedulas_10} cédula(s) de R$10,00'
      f'\nTotal de {cedulas_1} cédula(s) de R$1,00')
print('='*20)
print('Obrigado! Volte sempre!')