phrase = input('Enter a phrase: ').strip()
print(f"This phrase have {len(phrase.replace(' ',''))} characters")
print(f'The phrase in upper is: {phrase.upper()}')
print(f'The phrase in lower is: {phrase.lower()}')
print(f'{phrase:-^50}\n'
      f"It's a great phrase")