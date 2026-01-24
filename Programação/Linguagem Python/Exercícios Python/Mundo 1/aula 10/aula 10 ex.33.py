from statistics import median

n1 = int(input('Enter a number:'))
n2 = int(input('Enter another number:'))
n3 = int(input('Enter one more number:'))

if n1 <= n2 <= n3:
    a, b, c = n1, n2, n3
elif n2 <= n1 <= n3:
    a, b, c = n2, n1, n3
elif n2 <= n3 <= n1:
    a, b, c = n2, n3, n1
elif n1 <= n3 <= n2:
    a, b, c = n1, n3, n2
elif n3 <= n1 <= n2:
    a, b, c = n3, n1, n2
else:
    a, b, c = n3, n2, n1
print(f'{a} is less than {b}, and {b} is less than {c}')

#or

lista = [n1, n2, n3]

a = (max(lista))

b = median(lista)

c = (min(lista))
print(f'{c} is less than {b} and {b} is less than {a}')
