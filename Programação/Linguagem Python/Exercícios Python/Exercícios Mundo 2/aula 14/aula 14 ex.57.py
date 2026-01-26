sexo = ' '
while sexo not in 'MF':
    sexo = input('Qual o seu sexo? [M/F] ').upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('\033[31mInválido Tente novamente!\033[m')
print('Obrigado! tenha um ótimo dia!')