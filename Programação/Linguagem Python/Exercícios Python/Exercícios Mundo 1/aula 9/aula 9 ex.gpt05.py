word = input('Enter a Word: ').strip().capitalize()

print(f'Your word is: {word}')
if len(word) >=3:
    print(f'The first letter of the word is: {word[0]}\n'
          f'The second letter of the word is: {word[1]}\n'
          f'The third letter of the word is: {word[2]}')
    print('-'*46)
    print(f'The last letter of the word is: {word[-1]}\n'
          f'The penultimate letter of the word is: {word[-2]}\n'
          f'The third to last letter of the word is: {word[-3]}')
else:
    print(f'The first letter of the word is: {word[0]}\n'
          f'The last letter of the word is: {word[-1]}')

print(f'The word backwards is: {word[::-1]}')
