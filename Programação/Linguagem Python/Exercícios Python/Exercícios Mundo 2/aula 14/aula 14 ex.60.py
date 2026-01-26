n = int(input('Digite um número para saber sua fatorial: '))
while n < 0:
    print('\033[1;31mFatoriais de valores negativos não existe!\033[m')
    n = int(input('Digite um número para saber sua fatorial:'))
c = fatorial = n
if n == 0:
    fatorial = 1
    print('0! = 1')
else:
    print(f'{n}! = {n} x ', end ='')
    while c > 1:
        c -= 1
        fatorial *= c
        print(c, end= '')
        if c > 1:
            print(' x ' , end ='')
        else:
            print(f' = {fatorial}')
print(f'O fatorial de {n} é: {fatorial}')
