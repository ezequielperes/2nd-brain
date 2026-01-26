phrase = input('Enter a phrase: ').strip()
characters = len(phrase.replace(' ', ''))
print(f'This phrase have {characters} letters')
if characters > 10:
    print('\033[32mThis phrase is very long')
else:
    print('\033[31mThis phrase is short')