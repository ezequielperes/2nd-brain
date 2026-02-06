def escreva(txt):
    tamanho = len(txt) + 4
    print('~' * tamanho)
    print(txt.center(tamanho))
    print('~' * tamanho)


escreva('Gustavo Guanabara')

escreva('Curso de Python no Youtube')

escreva('CeV')