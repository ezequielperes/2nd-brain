def fatorial(n = 1, show=False):
    """
    -> Calculo o fatorial de um número.
    :param n:
    :param show: (Opcional) Mostrar ou não a conta
    :return:
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end ='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(5, True))