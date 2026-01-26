from time import sleep
opcao = 0

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite o 2° valor: '))

while opcao != 5:
    sleep(3)
    print('Você tem 5 opções:'
          '\n[1] Somar'
          '\n[2] Multiplicar'
          '\n[3] Maior'
          '\n[4] Novos Números'
          '\n[5] Sair'
          f'\nLembrando que o 1° valor é {valor1} e o 2° valor é {valor2}')
    sleep(7)
    opcao = int(input('Escolha: '))
    sleep(1)
    if opcao == 1:
        soma = valor1 + valor2
        print(f'\033[1;33m{valor1} + {valor2} = {soma}\033[m')
    elif opcao == 2:
        soma = valor1 * valor2
        print(f'\033[1;33m{valor1} * {valor2} = {soma}\033[m')
    elif opcao == 3:
        if valor1 > valor2:
            print(f'O maior valor é {valor1}')
        elif valor1 < valor2:
            print(f'O maior valor é {valor2}')
        else:
            print('Ambos são iguais!')
    elif opcao == 4:
        valor1 = int(input('Digite um valor:'))
        valor2 = int(input('Digite o 2° valor:'))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('\033[1;31mEntrada Inválida!\033[m')