n = input('Enter a number: ').zfill(4)

ninv = n[::-1]

print(f'the unit of this number is {ninv[0]}\n'
      f'the tens of this number is {ninv[1]}\n'
      f'the hundreds of this number is {ninv[2]}\n '
      f'the thousands of this number is {ninv[3]}')
