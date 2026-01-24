from time import sleep
valor1 = int(input('Digite um valor:'))
valor2 = int(input('Digite outro valor:'))
sleep(0.75)
soma = valor1 + valor2
multiplicar = valor1 * valor2
alt = 0
novo = 0
cont = 2
maior = 0
print('Você tem 5 alternativas do que fazer com estes números:')
while alt != 5:
    sleep(0.75)
    print('[1]Somar'
          '\n[2]Multiplicar'
          '\n[3]Maior'
          '\n[4]Novos Números'
          '\n[5]Sair do programa')
    sleep(2)
    alt = int(input(f'Digite uma opção\nLembrando que você já colocou {cont} valores: '))
    sleep(1)
    if alt == 5:
        print('Desligando Programa...')
        sleep(1)
    elif alt == 4:
        novo = int(input('Qual o novo número?'))
        cont+=1
    elif alt == 3:
        if valor1 >= valor2 and cont == 2:
            maior = valor1
        elif valor1 < valor2 and cont == 2:
            maior = valor2
        else:
            maior = novo
        print(f'O valor maior é: {maior}')
    elif alt == 2:
        if cont > 2:
            multiplicar *= novo
        print(f'A multiplicação dos {cont} valores é: {multiplicar}')
    elif alt == 1:
        soma += novo
        print(f'A soma desses {cont} valores são: {soma}')
    else:
        print('\033[31mEntrada Inválida!\033[m')