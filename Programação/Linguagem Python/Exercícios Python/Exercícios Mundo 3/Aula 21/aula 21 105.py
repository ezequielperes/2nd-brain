def notas(*n, sit=True):
    """
    -> Função para analisar notas e situações de aluno
    :param n: Uma ou mais notas do aluno
    :param sit: valor opicional, indicando se deveou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    print('-' *30)
    aluno = {
        'total': len(n),
        'maior': max(n),
        'menor': min(n),
        'media': sum(n)/len(n)
    }
    if sit:
        if aluno['media'] >= 7:
            aluno['situação'] = 'Boa'
        elif aluno['media'] >= 5:
            aluno['situação'] = 'Razoável'
        else:
            aluno['situação'] = 'Ruim'
    return aluno


print(notas(3, 10, 1 ))