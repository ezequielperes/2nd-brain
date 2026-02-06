def area(a, b):
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {a*b:.1f}m²')


print('Controle De Terrenos'.center(40))
print('-'*40)

l = float(input('Largura (m): '))
h = float(input('Altura (m): '))
area(l, h)