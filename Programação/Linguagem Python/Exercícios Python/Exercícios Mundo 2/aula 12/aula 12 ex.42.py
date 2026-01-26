a = int(input('Digite a medida do primeiro lado do triângulo: '))
b = int(input('Digite a medida do segundo lado do triângulo: '))
c = int(input('Digite a medida do terceiro lado do triângulo: '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Este triângulo é um equilátero')
    elif a != b and b != c and c != a:
        print('Este triângulo é um escaleno')
    else:
        print('Este triângulo é um Isósceles')
else:
    print('Estas medidas não formam um triângulo')