soma_idade = 0
f_maior = 0
entre_18_30 = 0
nome_f_maior = ''
homens_acima_media = 0
media_idade = 0

pessoas = int(input('Quantas pessoas vão entrar nos dados? '))

for c in range(1, pessoas+1):

    print(f'{f" {c}ª PESSOA ":-^20}')
    nome = input('Nome: ').strip().upper()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    soma_idade += idade

    #Mulher + idade
    if sexo == 'F' and c == 1:
        f_maior = idade
        nome_f_maior = nome
    else:
        if idade > f_maior and sexo == 'F':
            f_maior = idade
            nome_f_maior = nome

    #entre 18 e 30
    if 18 <= idade <= 30:
        entre_18_30 += 1
media_idade = soma_idade / pessoas
print(media_idade)
if homens_acima_media >= 1:
    print(homens_acima_media)
if f_maior >=1:
    print(nome_f_maior, f_maior)
if entre_18_30 >= 1:
    print(entre_18_30)
