valor = c = soma = 0
while valor != 999:
    valor = int(input('(Parada 999) Digite um valor:'))
    if valor != 999:
        c += 1
        soma += valor
print(f'A soma dos {c} números foi {soma} ')