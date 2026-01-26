from datetime import datetime
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input(f'em que ano a {c}ª pessoa nasceu? '))
    idade = datetime.now().year - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Tem {totmaior} pessoas totmaiores de 18 anos.\n'
      f'Tem {totmenor} pessoas totmenores de 18 anos.')