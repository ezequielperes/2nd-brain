l = float(input('Qual a largura da parede em metros: '))
h = float(input('Qual a altura da parede em metros:'))
A = l*h
print(f'Sua parede tem a dimensão de {l} x {h} e sua área é de {A}m²\n'
    f'A quantidade de litros de tinta necessária é de: {A/2}L')
