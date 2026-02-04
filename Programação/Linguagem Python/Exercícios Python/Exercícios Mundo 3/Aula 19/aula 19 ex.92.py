from datetime import datetime

ano_agora = datetime.now().year

dados = {
    'nome': input('Nome: ').strip().capitalize(),
    'idade': ano_agora - int(input('Ano de nascimento: ')),
    'ctps': int(input('Carteira De Trabalho (0 não tem): ')),
}

if dados['ctps'] > 0:
    ano_nascimento = ano_agora - dados['idade']
    dados['ano_contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Salário: R$'))
    dados['aposentadoria'] = dados['ano_contratação'] - ano_nascimento + 35
print('-='*30)

for k, v in dados.items():
    print(f' - {k.capitalize()}: {v}')
