def leiaint(msg):
    while True:
        numero_antigo = (input(msg))
        numero_novo = numero_antigo
        if '+' in numero_novo or '-' in numero_novo:
            numero_novo = numero_novo.replace('+','')
            numero_novo = numero_novo.replace('-', '')
        if numero_novo.isnumeric():
            numero_novo = int(numero_novo)
            if '-' in numero_antigo:
                numero_novo *= -1
            break
        print(f'\033[31mErro! Digite um número inteiro válido!\033[m')
    return numero_novo


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
