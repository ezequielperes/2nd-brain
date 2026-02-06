def voto(ano):
    from datetime import datetime

    atual = datetime.today().year
    idade = atual - ano
    if idade < 16:
        resposta = 'Negado'
    elif idade > 65 or 16 <= idade < 18:
        resposta = 'Opcional'
    else:
        resposta = 'Obrigatório'
    print(f'Com {idade} anos: Voto {resposta}')


ano_nasc = int(input('Ano de Nascimento: '))

voto(ano_nasc)
