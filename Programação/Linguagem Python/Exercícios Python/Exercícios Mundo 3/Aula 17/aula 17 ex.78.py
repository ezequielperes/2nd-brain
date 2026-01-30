valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
maior = max(valores)
menor = min(valores)
print(f'O valor maior foi {maior} e ele está nas posições:', end= ' ')
for i, valor in enumerate(valores):
    if valor == maior:
        print(f'{i}ª posição', end= ' ')
print(f'\nO menor valor foi {menor} e ele está nas posições:', end= ' ')
for i, valor in enumerate(valores):
    if valor == menor:
        print(f'{i}ª posição', end= ' ')
