m = float(input('Qual o seu peso? '))
h = float(input('Qual a sua altura em metros (m)? '))
imc = m / (h * h)
print(f'Seu Índice de Massa Corporal (IMC) é de {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do seu peso ideal!')
elif 18.5 <= imc < 25:
    print('Você está com o seu peso ideal!')
elif 25 <= imc < 30:
    print('Você está com Sobrepeso!')
elif 30 <= imc <= 40:
    print('Você está com Obesidade!')
else:
    print('Você está com Obesidade Mórbida!')
