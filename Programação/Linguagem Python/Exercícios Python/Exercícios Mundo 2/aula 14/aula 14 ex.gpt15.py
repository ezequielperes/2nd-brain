soma = c = 0
n = int(input('Digite um número para somar (0 para parar): '))

while n != 0:
    c += 1
    soma += n
    n = int(input('Digite um número para somar (0 para parar): '))
print(f'A soma dos {c} números foi de: {soma}')