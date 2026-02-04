alunos_notas = []
while True:
    qnt_notas = int(input('Quantidade de notas: '))
    if qnt_notas > 0:
        break
    print('Inválido, tente novamente')
while True:
    nome = input('Informe o nome: ').capitalize()
    notas = []
    for c in range(qnt_notas):
        while True:
            nota = float(input('Informe a nota [0 a 10]: '))
            if 0 <= nota <= 10:
                break
            print('Inválido, Tente novamente!')
        notas.append(nota)
    media = sum(notas) / qnt_notas
    alunos_notas.append([nome, notas ,media])
    while True:
        resposta = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if resposta in 'SN':
            break
    if resposta == 'N':
        break
    print('-'*30)
print('-='*30)
print(f'No. NOME {"MÉDIA":>15}')
print('-'*30)
for n, nome_media in enumerate(alunos_notas):
    print(f'{n}  {nome_media[0]:<15} {nome_media[2]:>5.2f}')
print('-'*30)
print('-='*30)
while True:
    while True:
        aluno = int(input('Mostar notas de qual aluno (999 para parar)? [No.] '))
        if aluno in range(0, len(alunos_notas)) or aluno == 999:
            break
        print('Inválido, Tente novamente')
    if aluno == 999:
        break
    print('-'*30)
    print(f'As notas do(a) aluno(a) {alunos_notas[aluno][0]} é: {alunos_notas[aluno][1]}')
print('-='*30)
print('Programa encerrado! Volte sempre!')