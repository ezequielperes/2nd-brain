print('Lets find the hypotenuse')

catop = float(input('enter a number of the opposite side: '))
catad = float(input('enter a number of the adjacent side: '))

print(f'The hypotenuse is {((catop**2 + catad**2)**(1/2)):.1f}')

'''or'''

from math import hypot

print('lets find the hypotenuse')
co = float(input('enter a number of the opposite side: '))
ca = float(input('enter a number of the adjacent side: '))

print(f'The hypotenuse is {hypot(co, ca):.2f}')
