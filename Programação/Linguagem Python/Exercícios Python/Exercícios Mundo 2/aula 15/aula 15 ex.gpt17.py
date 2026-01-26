soma = c = 0
while True:
    n = int(input('Digite um número para somar (Nº negativo para parar): '))
    if n < 0:
        break
    soma += n
    c += 1
print(f'A soma dos {c} números foi de: {soma}')