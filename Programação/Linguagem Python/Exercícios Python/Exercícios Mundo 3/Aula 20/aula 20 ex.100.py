from random import randint
from time import sleep
def sorteia(qnt_sorteio):
    lista_numeros = []
    print(f'Sorteando {qnt_sorteio} valores da lista:', end=' ')
    for c in range(qnt_sorteio):
        numero = randint(1, 10)
        lista_numeros.append(numero)
        print(numero, end = ' ')
        sleep(0.5)
    print('Pronto!')
    return lista_numeros

def soma_par(lista_numeros):
    soma = sum(par for par in lista_numeros if par % 2 == 0)
    print(f'Somando os valores pares de {lista_numeros}, temos: {soma}')

numeros = sorteia(5)
soma_par(numeros)

