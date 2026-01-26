name = input('Enter a name: ').strip().title()

divided = name.split()
firstname = divided[0]
lastname = divided[-1]

print(f'Your first name is {firstname}')
print(f'Your last name is {lastname}')