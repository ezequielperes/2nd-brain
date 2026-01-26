n1 = int(input('Digite a nota da primeira prova'))
n2 = int(input('Digite a nota da segunda prova'))
while n1 not in range(0, 11) or n2 not in range(0, 11):
    print('\033[31mEntrada inválida\033[m')
    n1 = int(input('Digite a nota da primeira prova'))
    n2 = int(input('Digite a nota da segunda prova'))
media = (n1 + n2) / 2
if media < 5:
    print('Reprovado')
elif 5 <= media < 7:
    print('Recuperação')
else:
    print('Aprovado')