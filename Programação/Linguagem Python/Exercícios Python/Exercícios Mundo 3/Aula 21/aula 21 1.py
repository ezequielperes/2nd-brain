def contador(i=0, f=0, p=0):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c+=p
    print('Fim!')

#Utilização do Help
help(contador)

#Utilização global
def funcao():
    global n1
    n1 = 4
    print(f'N1 Escopo local vale {n1}')


n1= 2
print(f'N1 Escopo global vale {n1}')
funcao()

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'\nOs Resultados foram {r1}, {r2} e {r3}')
