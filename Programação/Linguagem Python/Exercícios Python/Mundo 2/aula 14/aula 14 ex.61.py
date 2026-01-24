a1 = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão? '))
a10 = a1 + 10 * r
while a1 != a10:
    print(a1, end= f' ')
    a1 += r
