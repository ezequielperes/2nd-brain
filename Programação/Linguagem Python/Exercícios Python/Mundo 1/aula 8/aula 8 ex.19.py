from random import choice
print("who's going to erase the blackboard?")

a1 = input('first student: ')
a2 = input('second student:')
a3 = input('third student: ')
a4 = input('fourth student:')

lista = [a1, a2, a3, a4]

print(f'the student who will erase the blackboard is {choice(lista)}!')