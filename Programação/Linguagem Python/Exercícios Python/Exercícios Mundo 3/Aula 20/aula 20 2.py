def contador(*num):
    print(num, len(num))


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 8, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

def soma(*numeros):
    s = 0
    for n in numeros:
        s += n
    print(f'Somando os valores {numeros}, temos {s}')

soma(6, 8, 9)
soma(1, 2, 3)
soma(4, 2, 8, 9)
