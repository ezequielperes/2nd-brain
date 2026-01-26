maioridade = 0
m_cadastrados = 0
f_menos_vinte = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        maioridade += 1
    sexo = input('Sexo: [M/F] ').strip().upper()[0]
    while sexo not in 'MF':
        print('\033[31mInválido Digite novamente!\033[m')
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    if sexo == 'M':
        m_cadastrados += 1
    if sexo == 'F' and idade < 20:
        f_menos_vinte += 1
    resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while resposta not in 'SN':
        print('\033[31mInválido Digite novamente!\033[m')
        resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
    print('-'*20)
    if resposta == 'N':
        break
print(f'Foram {maioridade} pessoas cadastradas com mais de 18 anos'
      f'\nForam {m_cadastrados} homens cadastrados'
      f'\nForam {f_menos_vinte} mulheres com menos de 20 anos cadastradas')

