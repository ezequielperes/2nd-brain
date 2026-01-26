termo = -1
c = 0
while termo != 0:
    termo = int(input('Quantidade de termos que você quer mostrar: '))
    c += termo
    if termo != 0:
        a1 = int(input('Digite o primeiro termo: '))
        r = int(input('Digite a razão da PA: '))
        cont = 0
        while cont != termo:
            cont += 1
            print(a1, end=' ')
            a1 += r

print(f'FIM, foi mostrado {c} termos na tela')