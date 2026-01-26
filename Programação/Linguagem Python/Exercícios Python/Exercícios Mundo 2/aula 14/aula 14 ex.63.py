print('-'*30)
print('Sequência de Fibonacci'.center(30))
print('-'*30)
n = int(input('Quantos termos de Fibonacci você quer mostrar?: '))
c = 0
fibo = 0
fiboant = 1
while c < n:
    c += 1
    print(fibo, end= '')
    if c < n:
        print(' -> ', end='')
    fiboant, fibo = fibo, fibo + fiboant