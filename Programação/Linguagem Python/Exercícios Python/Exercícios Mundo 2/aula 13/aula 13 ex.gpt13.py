inicio = int(input('Qual vai ser o ínicio da contagem? '))
fim = int(input('Qual vai ser o fim da contagem? '))
passo = abs(int(input('Qual vai ser o passo da contagem? ')))
while passo == 0:
    print('\033[31mPasso inválido! Não pode ser 0 (zero)!\033[m')
    passo = abs(int(input('Qual vai ser o passo da contagem?')))
if inicio < fim:
    for c in range( inicio, fim + 1, passo):
        print(c, end= ' -> ')
else:
    for c in range( inicio, fim - 1, -passo):
        print(c, end= ' -> ')
print('Fim!')
