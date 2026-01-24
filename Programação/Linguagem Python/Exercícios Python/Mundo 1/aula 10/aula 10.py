n = (float(input('Digite sua nota da prova: ')))
if 0 <= n < 5:
    print('Que vergonha... não passou\n:(')
elif 5 <= n < 6:
    print('Passou na rapa em, CUIDADO!!!\n>:(')
elif 6 <= n < 9:
    print('Parabéns, você passou !!!\n:)')
elif 9 <= n <= 10:
    print('Passou e passou GOSTOSO !!!\n ͡o ͜ʖ ͡o')
else:
    print('Nota inválida\n>:(')