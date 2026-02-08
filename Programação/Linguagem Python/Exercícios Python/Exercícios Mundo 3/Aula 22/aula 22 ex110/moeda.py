def formatado(valor = 0.0,formatando=True,moeda= 'R$'):
    if formatando:
        return f'{moeda}{valor:.2f}'.replace('.', ',')
    else:
        return valor


def aumentar(n = 0.0, taxa=0,formato=True, moeda= 'R$'):
    """
    ->aumentar o param n com o aumentando em %
    :param n: valor
    :param taxa: aumentando o valor em %
    :param formato: formatar o valor em monetário
    :param moeda: moeda do valor
    :return: valor aumentado
    """
    num = n + (n * taxa/100)
    return formatado(num, formato, moeda)


def diminuir(n = 0.0, taxa = 0, formato=True, moeda= 'R$'):
    """
    ->Diminui o param n com o diminuindo em %
    :param n: valor
    :param taxa: Diminuindo o valor em %
    :param formato: formatar o valor em monetário
    :param moeda: moeda do valor
    :return: valor diminuido
    """
    num = n - (n * taxa/100)
    return formatado(num, formato, moeda)


def dobro(n=0, formato=True, moeda='R$'):
    """
    -> Dobro do param n
    :param n: valor
    :param formato: formatar o valor em monetário
    :param moeda: moeda do valor
    :return: valor x 2
    """
    num = n * 2
    return formatado(num, formato, moeda)


def metade(n = 0, formato=True, moeda= 'R$'):
    """
    -> Metade do param n
    :param n: valor
    :param formato: formatar o valor em monetário
    :param moeda: moeda do valor
    :return: valor / 2
    """
    num = n / 2
    return formatado(num, formato, moeda)


def resumo(n=0, taxa_aumento=0, taxa_reducao=0, formato=True, moeda= 'R$'):
    print('-'*40)
    print('Resumo Do Valor'.center(40))
    print('-'*40)
    print(f'{"Preço analisado:":<30} {formatado(n, formato, moeda)}'
    f'\n{"Dobro do preço:":<30} {dobro(n, formato, moeda)}'
    f'\n{"Metade do preço:":<30} {metade(n, formato, moeda)}'
    f'\n{f"{taxa_aumento}% do aumento:":<30} {aumentar(n, taxa_aumento, formato, moeda)}'
    f'\n{f"{taxa_reducao}% de redução:":<30} {diminuir(n, taxa_reducao, formato, moeda)}')
    print('-'*40)

