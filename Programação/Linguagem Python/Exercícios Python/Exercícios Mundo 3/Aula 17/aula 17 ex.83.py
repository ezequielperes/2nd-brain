expressao = list(input('Digite a expressão: '))
resposta = 'válida'
if expressao.count('(') == expressao.count(')'):
    parenteses = list()
    for caractere in expressao:
        if caractere == '(' or caractere == ')':
            parenteses.append(caractere)
    soma = 0
    for c in range(0, len(parenteses)):
        if parenteses[c] == '(':
            soma += 1
        else:
            soma -= 1
        if soma < 0 or c == len(parenteses) -1 and soma > 0:
            resposta = 'inválida'
            break
        print(soma)
else:
    resposta = 'inválida'

print(f'Sua expressão é {resposta}!')
