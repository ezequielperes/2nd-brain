def fatorial (num=1):
    f = 1
    for c in range(num, 0 , -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

print()
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

def parouimpar(num=0):
    if num % 2 == 0:
        return True
    else:
        return False

print()
n = int(input('Digite um número '))
print(parouimpar(n))

if parouimpar(n):
    print('É par!')
else:
    print('Não é par!')