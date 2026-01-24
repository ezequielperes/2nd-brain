"""
frase = input('Digite uma frase:').strip().upper().replace(' ', '')
print(f'A frase {frase} ao contrário fica {frase[::-1]}')
if frase == frase[::-1]:
    print('Esta frase é um palíndromo')
else:
    print('Esta frase não é um palíndromo')
"""

#or

frase = input('Digite uma frase: ').upper().strip().replace(' ', '')
inverso = ''
for letra in range(len(frase) -1, -1, -1):
    inverso += frase[letra]
print(f'A frase que você escreveu é: {frase}. Ela invertida ficará {inverso}')
if inverso == frase:
    print('Esta frase é um palíndromo')
else:
    print('Esta frase não é um palíndromo')