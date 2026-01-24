sexo = ''
r = ''
while r != 'S':
    r = ''
    sexo = input('Qual o seu sexo [M/F]: ').upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('\033[31mDigite novamente!\033[m')
    else:
        while r != 'S' and r != 'N':
            r = input(f'Você tem certeza que você tem o sexo ({sexo}) ? [S/N]: ').upper().strip()
            if r != 'S' and r != 'N':
                print('\033[31mDigite novamente!\033[m')

print('Obrigado! Tenha um ótimo dia!')