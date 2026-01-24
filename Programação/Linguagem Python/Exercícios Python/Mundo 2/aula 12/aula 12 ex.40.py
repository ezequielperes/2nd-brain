n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print(f'Sua nota foi \033[1;32m{media:.1f}\nAPROVADO')
elif media >=5:
    print(f'Sua nota foi \033[1;33m{media:.1f}\nRECUPERAÇÃO')
else:
    print(f'Sua nota foi \033[1;31m{media:.1f}\nREPROVADO')