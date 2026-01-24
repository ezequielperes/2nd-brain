from datetime import datetime

ano = int(input('Qual a sua data de nascimento ? '))

idade = int(datetime.now().year) - ano
print(f'O atleta tem: {idade} anos')
if idade <=9:
    print('Você está na categoria Mirim da natação!')
elif idade <=14:
    print('Você está na categoria Infantil da natação!')
elif idade <= 19:
    print('Você está na categoria Junior da natação!')
elif idade <=25:
    print('Você está na categoria Sênior da natação!')
else:
    print('Você está na categoria Master da natação!Master')