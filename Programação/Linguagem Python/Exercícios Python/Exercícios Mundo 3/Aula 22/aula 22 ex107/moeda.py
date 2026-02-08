def aumentar(n, taxa):
    """
    ->aumentar o param n com o aumentando em %
    :param n: valor
    :param taxa: aumentando o valor em %
    :return: valor aumentado
    """
    return n + (n * taxa/100)


def diminuir(n, taxa):
    """
    ->Diminui o param n com o diminuindo em %
    :param n: valor
    :param taxa: Diminuindo o valor em %
    :return: valor diminuido
    """
    return n - (n * taxa/100)


def dobro(n):
    """
    -> Dobro do param n
    :param n: valor
    :return: valor x 2
    """
    return n * 2


def metade(n):
    """
    -> Metade do param n
    :param n: valor
    :return: valor / 2
    """
    return n / 2
