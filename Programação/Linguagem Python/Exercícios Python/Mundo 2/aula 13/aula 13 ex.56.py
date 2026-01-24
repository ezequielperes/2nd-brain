nome_velho = ''
velho = 0
media_idade = 0
f_menor = 0
homens = 0
pessoas = int(input('Quantas pessoas vão entrar nos dados? '))

for c in range(1, pessoas + 1):

    print(f'{f" {c}ª PESSOA ":-^20}')
    nome = input('Nome: ').strip().upper()
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').strip().upper()

    media_idade += idade

    if sexo == 'M':
        homens += 1

    if c == 1 and sexo == 'M':
        velho = idade
        nome_velho = nome
    else:
        if idade > velho and sexo == 'M':
            velho = idade
            nome_velho = nome
    if idade < 20 and sexo == 'F':
        f_menor += 1

print(f'A média de idade do grupo é de {media_idade / pessoas}')

if homens >= 1:
    print(f'O homem mais velho tem {velho} e se chama: {nome_velho}')

print(f'Ao todo são {f_menor} mulheres com menos de 20 anos')

