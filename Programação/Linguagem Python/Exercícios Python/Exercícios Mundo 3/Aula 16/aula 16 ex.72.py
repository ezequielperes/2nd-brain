n_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
             'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
             'Dezenove', 'Vinte')
while True:

    while True:
        n = int(input('Digite um número de 0 a 20:'))
        if 0 <= n <= 20:
            break
        print('\033[31mValor Inválido, Digite novamente!\033[m')

    print(f'Você escolheu o número {n_extenso[n]}')

    while True:
        resposta = input('Quer continuar? [S/N]: ').upper().strip()[0]
        if resposta in 'SN':
            break
        print('\033[31mInválido, Digite novamente!\033[m')

    if resposta == 'N':
        break

print('Programa finalizado!')