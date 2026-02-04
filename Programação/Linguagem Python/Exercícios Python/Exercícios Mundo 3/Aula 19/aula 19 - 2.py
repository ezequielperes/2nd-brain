#Obs: Cortei em 2 partes não por ser algo complexo, mas algo muito utilizado
#Logo, se é muito utilizado, tem que ser bem exercitado!

#Teste 1
pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22
}
pessoas['peso'] = 95
print(pessoas)

for key, value in pessoas.items():
    print(f'{key} = {value}')

#Teste 2
print()
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {
    'uf':'São Paulo',
    'sigla': 'SP'
}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla'])

#Teste 3
estado = {}
pais = []
for _ in range(3):
    estado['uf'] = input('Nome Do estado: ').title().strip()
    estado['sigla'] = input('Sigla do estado: ').upper().strip()
    pais.append(estado.copy())
for estado in pais:
    for v in estado.values():
        print(v, end=' ')
    print()