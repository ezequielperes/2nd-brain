from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim:
        passo = -abs(passo)
    elif inicio < fim:
        passo = abs(passo)
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        fim -= 1
    elif inicio < fim:
        fim += 1
    for c in range(inicio, fim, passo ):
        print(c, end= ' ')
        sleep(0.25)
    print('Fim !')


contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)
