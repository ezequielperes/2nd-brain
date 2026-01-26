frase = input('Enter a phrase: ').lower()


print(frase.count('a')+frase.count('ã')+frase.count('â')+frase.count('á')+frase.count('à'))
print(min(frase.find('a'), frase.find('ã'), frase.find('â'), frase.find('á'), frase.find('à')))
print(max(frase.rfind('a'), frase.rfind('ã'), frase.rfind('â'), frase.rfind('á'), frase.rfind('à')))
