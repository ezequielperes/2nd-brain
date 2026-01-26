from random import shuffle
print("what's presentation order?")

s1 = input('first student: ')
s2 = input('second student: ')
s3 = input('third student: ')
s4 = input('fourth student: ')

lista = [s1, s2, s3, s4]
shuffle(lista)

print('the presentation order is:\n'
     f'{lista}')
