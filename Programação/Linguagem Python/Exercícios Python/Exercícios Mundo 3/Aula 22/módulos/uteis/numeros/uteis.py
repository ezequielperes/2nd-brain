def fatorial(numero, show=False):
    f = 1
    for c in range(numero, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(f'x ', end='')
            else:
                print('= ', end='')
        f *= c

    return f


def dobro(numero):
    return numero * 2

def triplo(numero):
    return numero * 3
