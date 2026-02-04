#Obs: Cortei em 2 partes não por ser algo complexo, mas algo muito utilizado
#Logo, se é muito utilizado, tem que ser bem exercitado!

# transformando uma variável em dicionário
dados = dict()

#or

dados = {}

#Colocando chaves e valores na variável dados
dados = {'nome':'Pedro', 'idade':25}

#or

dados = {
    'nome': 'Pedro',
    'idade': 25
}

#Mostrando um Valor
print(dados['nome'])
print(dados['idade'])

#Adicionando uma chave e um valor
print()
dados['sexo'] = 'M'
print(dados)
print(dados['sexo'])

#Excluindo uma chave
print()
del dados['idade']
print(dados)

filme1 = {'titulo':'Star Wars',
         'ano': 1977,
         'diretor':'George Lucas'
}

#Mostra somente os valores
print()
print(filme1.values())

#Mostra somente as chaves
print()
print(filme1.keys())

#Mostra os valores e as chaves
print()
print(filme1.items())

#Utilizando Loops com dicionários
print()
for key, value in filme1.items():
    print(f'O {key} é {value}')

#Tuplas, Listas, e Dicionários, podem ser utilizados em conjunto
filme2 = {
    'titulo': 'Avengers',
    'ano': 2012,
    'diretor': 'Joss Whedon'
}
filme3 = {
    'titulo': 'Matrix',
    'ano': 1999,
    'diretor': 'Wachowski'
}
locadora = list()
locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)

print()
print(locadora)
for c, filme in enumerate(locadora):
    print()
    print('-'*5 ,f'{c+1}º filme', '-'*5)

    for k, v in filme.items():
        print(f'O {k} é {v}')
    print('-'*20)