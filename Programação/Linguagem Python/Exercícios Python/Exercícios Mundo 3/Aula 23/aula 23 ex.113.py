def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('\033[33m\nO usuário preferiu não digitar o número\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número inteiro válido!\033[m')
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = input(msg).replace(',','.')
            num = float(n)
        except KeyboardInterrupt:
            print('\033[33mO usuário preferiu não digitar o número\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número real válido!\033[m')
            continue
        else:
            return num


inteiro = leiaint('Digite o número inteiro: ')
real = leiafloat('Digite um número real: ')
print(f'O número inteiro foi {inteiro} e o real foi {real}')

