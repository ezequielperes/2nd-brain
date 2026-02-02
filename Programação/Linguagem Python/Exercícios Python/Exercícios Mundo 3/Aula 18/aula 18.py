dados = list()

dados.append('Pedro')
dados.append(25)

print(dados)
print(dados[0])
print(dados[1])

#Lista dentro de outra lista
pessoas = [['Maria', 19], ['João', 32]]
print(pessoas)

#Inserindo uma lista dentro de uma lista (funciona com .append também, na verdade os comandos são os mesmos)
pessoas.insert(0,dados[:])
print(pessoas)
pessoas.clear()

#Pode ser colocado
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas)

#Escrevendo a lista de Pedro
print(pessoas[0])

#Colocando um dado da lista de pedro
print(pessoas[0][1])

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos')

#Input/Entrada de dados
pessoas = []
dado = []
for c in range(0, 5):
    dado.append(input('Nome: '))
    dado.append(int(input('idade:')))
    pessoas.append(dado[:])
    dado.clear()
pessoas[1].sort()
print(pessoas)

maior = menor = 0
for p in pessoas:
    if p[1] >= 18:
        print(f'\n{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'\n{p[0]} é menor de idade')
        menor += 1
print(f'Temos {maior} maiores de idade'
      f'\nTemos {menor} menores de idade')