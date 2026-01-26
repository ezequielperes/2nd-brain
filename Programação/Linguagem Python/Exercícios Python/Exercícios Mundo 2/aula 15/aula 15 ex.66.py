soma = c = 0
while True:
    n = int(input('Digite um número (\033[33m999 para parar\033[m): '))
    if n == 999:
        break
    soma += n
    c += 1
print(f'Você digitou {c} números e a soma entre eles é {soma}')