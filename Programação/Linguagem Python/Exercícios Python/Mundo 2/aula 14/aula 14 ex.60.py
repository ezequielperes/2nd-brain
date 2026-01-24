n = int(input('Digite um número para saber sua fatorial: '))
mult = n
if n == 0:
    mult = 1
else:
    for c in range(n-1, 0 , -1):
        mult *= c
    print(f'A fatorial do número {n} é de {mult}')

#or

num = int(input('Digite um número para saber sua fatorial:'))
mult = num
c = num
if num == 0:
    mult = 1
else:
    while c != 1:
        c-=1
        mult *= c
        
print(f'A fatorial do número {num} é : {mult}')
