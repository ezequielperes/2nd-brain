from time import sleep
num = int(input('Enter a number:'))
print('You have 3 choices:')
sleep(1)
print('\033[34m1 -> convert you number to binary')
sleep(1)
print('\033[33m2 -> convert you number to octal')
sleep(1)
print('\033[32m3 -> convert you number to hexadecimal')
sleep(1)
num_choice = int(input('\033[35mChoice:'))
print('\033[36mProcessing your choice...')
sleep(0.8)
if num_choice == 1:
    print(f'\033[34mThis number in Binary is {bin(num)[2:]}')
elif num_choice == 2:
    print(f'\033[33mThis number in Octal is: {oct(num)[2:]}')
elif num_choice == 3:
    print(f'\033[32mThis number in Hexadecimal is: {hex(num)[2:]}')
else:
    print(f"\033[31mThis isn't a valid option")
