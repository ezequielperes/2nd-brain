num = int(input('Enter a number: '))
print(f'The double of {num} is: {num*2}\n'
      f'The triple of {num} is: {num*3}\n'
      f'The square root of {num} is: {num**(1/2):.2f}')
if num % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')
