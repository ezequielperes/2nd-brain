from time import sleep


def linha(tamanho = 40):
    print('-' * tamanho)

def titulo(*txt, tamanho = 40):
    sleep(0.25)
    linha(tamanho)
    sleep(0.25)
    for texto in txt:
        print(texto.center(tamanho))
    sleep(0.25)
    linha(tamanho)
    sleep(0.25)