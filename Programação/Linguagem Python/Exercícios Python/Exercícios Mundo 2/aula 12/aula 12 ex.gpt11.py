idade = int(input('Digite sua idade: '))
while idade not in range(1, 121):
    print('\033[31mDigite uma idade válida!\033[m')
    idade = int(input('Digite sua idade: '))
if idade < 12:
    print('Criança')
elif 12 <= idade <= 17:
    print('Adolescente')
elif 18 <= idade <= 59:
    print('Adulto')
else:
    print('Idoso')