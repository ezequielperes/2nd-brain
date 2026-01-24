num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number:'))
if num1 > num2:
    print(f'The number \033[32m{num1}\033[m is greater than \033[31m{num2}')
elif num1 < num2:
    print(f'The number \033[32m{num2}\033[m is greater than \033[31m{num1}')
else:
    print(f'\033[33mThe numbers are equals')
