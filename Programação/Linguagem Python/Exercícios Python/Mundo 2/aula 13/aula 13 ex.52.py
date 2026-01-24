n = int(input('Digite um número: '))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'\n\033[mEste número é divisivel por {total} números')
if total == 2:
    print('Este número é primo!')
else:
    print('Este número não é primo!')