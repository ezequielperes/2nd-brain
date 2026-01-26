from time import sleep
while True:
    n = int(input('Quer ver a tabuada de qual valor (valor \033[33mnegativo (-)\033[m para \033[33mparar\033[m):? '))
    print('-' * 20)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}'.center(20))
        sleep(0.5)
    print('-'*20)
print('Finalizado! Volte sempre!')
