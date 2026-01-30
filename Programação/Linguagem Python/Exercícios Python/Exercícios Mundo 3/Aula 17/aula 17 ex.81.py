valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    while True:
        resposta = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if resposta in 'SN':
            break
        print('Resposta inválida, tente novamente!')

    if resposta == 'N':
        break
    print('-'*40)

print('-='*20)
print(f'Você digitou {len(valores)} valores')
print('-'*40)

valores_decrescente = valores[:]
valores_decrescente.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente foram'
      f'\n{valores_decrescente}')

print('-'*40)
print('Os valores digitados sem formatação foi:'
      f'\n{valores}')
print('-'*40)

if 5 in valores:
    print('O valor 5 apareceu na', end= ' ')
    for i, valor in enumerate(valores):
        if valor == 5:
            print(f'{i}ª posição', end=' ')
else:
    print('O valor 5 não foi digitado na lista')
