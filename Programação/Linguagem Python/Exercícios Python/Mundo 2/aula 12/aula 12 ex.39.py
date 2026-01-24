from datetime import datetime

mes_agora = int(datetime.now().month)
ano_agora = int(datetime.now().year)

ano_idade = int(input('Em que ano você nasceu?'))

ano_vai_fazer_18 = ano_idade + 18

proximo_alistamento = 12 - mes_agora + 1

ate_alistamento = (ano_vai_fazer_18 * 12) - (ano_agora * 12 - mes_agora)

# ano de nascimento inválido
if ano_idade > ano_agora:
    print('Ano de nascimento inválido')

# é o ano que vai fazer 18 e é mes de alistament
elif ano_vai_fazer_18 == ano_agora and mes_agora <= 6:
    print('Você pode se alistar agora!')

# é o ano que vai fazer 18 mas ja passou o mes de alistamento
elif ano_vai_fazer_18 == ano_agora and mes_agora > 6:
    print('Já foi o tempo de se alistar')
    print(f'O próximo alistamento é daqui {proximo_alistamento} meses')

# ja fez 18 e é mês de alistamento
elif ano_vai_fazer_18 < ano_agora and mes_agora <= 6:
    print('Você pode se alistar agora!')
    print('Como você já tem +18 voce terá que pagar uma multa')
    print(f'Seu ano de alistamento era o ano de {ano_vai_fazer_18}')

# ja fez 18 e não é mês de alistamento
elif ano_vai_fazer_18 < ano_agora and mes_agora > 6:
    print('Já foi o tempo de se alistar')
    print('Como você já tem +18 voce terá que pagar uma multa quando fizer')
    print(f'Seu ano de alistamento era o ano de {ano_vai_fazer_18}')
    print(f'O próximo alistamento será daqui {proximo_alistamento} meses')

# Ainda não fez 18 ano_vai_fazer_18 > ano_agora:
else:
    print('você ainda não pode se alistar')
    print(f'Seu ano de alistamento será em {ano_vai_fazer_18}')
    print(f'Falta {ate_alistamento // 12} anos e {ate_alistamento % 12} meses')
