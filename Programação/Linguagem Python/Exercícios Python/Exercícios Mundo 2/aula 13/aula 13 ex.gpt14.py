soma = 0
i = int(input('Quantos números você deseja somar? '))
for c in range(1, i + 1):
    n = int(input('Digite um número'))
    soma += n
print(f'A soma dos {i} números foi de: {soma}')