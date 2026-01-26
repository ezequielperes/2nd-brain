from time import sleep
valor = float(input('Digite o valor do produto: R$'))
print('Qual será sua forma de pagamento?')
sleep(1)
print('1 -> À vista dinheiro e/ou cheque: 10% de desconto')
sleep(1)
print('2 -> À vista no cartão: 5% de desconto')
sleep(1)
print('3 -> 2x no cartão: preço normal')
sleep(1)
print('4 -> 3x ou mais no cartão: 20% de juros')
sleep(1)
cond_pag = int(input('\033[35mEscolha a forma de pagamento de 1 a 4: \033[m'))
if cond_pag == 1:
    print(f'O valor do produto foi de R${valor:.2f} para R${valor * 0.9:.2f}')
elif cond_pag == 2:
    print(f'O valor do produto foi de R${valor:.2f} para R${valor * 0.95:.2f}')
elif cond_pag == 3:
    print(f'Parcelando em 2x ficará R${valor/2:.2f} o valor das parcelas')
elif cond_pag == 4:
    parcela = int(input('Em quantas parcelas? '))
    print(f'Parcelando em {parcela} ficará R${valor * 1.2 / parcela:.2f} o valor das parcelas'
          f'O pagamento total com os juros ficará R${valor *1.2}')
else:
    print('\033[31mCondição de pagamento inválida!')
