print('-'*30)
print('10 primeiros termos de uma PA'.center(30))
print('-'*30)
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 0
while c < 10:
    c += 1
    print(f'{a1}', end='')
    if c < 10:
        print(' -> ', end='')
    a1 += r