resposta = int(input('Parte 1 / parte 2 / parte 3? \n[1/2/3]: '))
if resposta == 1:
    #Litas começam e terminam com colchetes
    n = [2, 5, 9, 1]
    print('\nn = [2, 5, 9, 1]\n',n)

    #Listas são mutáveis diferente das Tuplas, nesse caso trocou-se o objeto do index 2 que era 9 para 3
    n[2] = 3
    print('\nn[2] = 3\n',n)

    #.append() adiciona um novo objeto em um novo index
    n.append(4)
    print('\nn.append(4)\n',n)

    #.sort deixa em ordem crescente os objetos
    n.sort()
    print('\nn.sort()\n',n)

    #.sort(reverse=True deixa em ordem decrescente os objetos
    n.sort(reverse=True)
    print('\nn.sort(reverse=True)\n',n)

    #.insert adiciona um novo objeto a lista em um index específico
    n.insert(4, 0)
    print('\nn.insert(4,0)\n',n)

    n.sort()
    print('\nn.sort()\n',n)

    #.pop() excluí o último index
    n.pop()
    print('\nn.pop()\n',n)

    #.pop(index) excluí um index específico
    n.pop(1)
    print('\nn.pop(1)\n',n)

    #.remove(obj) exclui apenas um objeto específico da lista, não exclui mais de um, apenas com laços
    #OBS: caso não tenha o objeto especificado ele vai dar erro
    n.remove(3)
    print('\nn.remove(3)\n',n)
    # propositalmente SEM verificação pra mostrar o erro do .remove()
    n.remove(3)
    print('\nn.remove(3)\n',n)
elif resposta == 2:
    valores = list()
    valores.append(5)
    valores.append(10)
    valores.append(7)
    for i, valor in enumerate(valores):
        print(f'na posicção {i} enconterei o valor {valor} ')
    print('Cheguei no final da lista')

    #Cria uma lista do zero
    valores.clear()

    #Cria uma lista do zero
    valores = list()
    for c in range(0, 5):
        valores.append(int(input('Digite um valor: ')))
    print(valores)
else:
    a = [2, 3, 4 ,7, 10]
    b = a
    print(f'\nLista A: {a}'
          f'\nLista B: {b}')

    #Quando você faz uma lista uma váriável receber uma lista as duas ficam interligadas para sempre!
    #Se você trocar um valor de uma lista, a outra tbm vai trocar
    b[2] = 8
    print(f'\nLista A: {a}'
          f'\nLista B: {b}')
    #Quando você faz um fatiamento em vez de só receber a váriavel lista, o python entende que você só quer apenas copiar
    #E não interligar
    b = a[:]
    b[3] = 21
    print(f'\nLista A: {a}'
          f'\nLista B: {b}')