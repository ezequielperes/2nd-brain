def aumentar(n = 0, taxa = 0):
    """
    ->aumentar o param n com o aumentando em %
    :param n: valor
    :param taxa: aumentando o valor em %
    :return: valor aumentado
    """
    return n + (n * taxa/100)


def diminuir(n = 0, taxa = 0):
    """
    ->Diminui o param n com o diminuindo em %
    :param n: valor
    :param taxa: Diminuindo o valor em %
    :return: valor diminuido
    """
    return n - (n * taxa/100)


def dobro(n = 0):
    """
    -> Dobro do param n
    :param n: valor
    :return: valor x 2
    """
    return n * 2


def metade(n = 0):
    """
    -> Metade do param n
    :param n: valor
    :return: valor / 2
    """
    return n / 2


def moeda(valor = 0, valor_monetário = 'R$'):
    return f'{valor_monetário}{valor:.2f}'.replace('.', ',')
