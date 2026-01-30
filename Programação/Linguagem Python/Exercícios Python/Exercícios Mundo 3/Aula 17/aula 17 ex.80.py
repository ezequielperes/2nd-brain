valores = list()
for c in range(0, 100):
    valor = (int(input('Digite um valor: ')))
    if c == 0 or valor >= valores[-1]:
        print(f'Valor {valor} na {c}ª posição da lista...')
        valores.append(valor)
    else:
        for i in range(0, len(valores)):
            if valor <= valores[0] or valores[i-1] <= valor <= valores[i]:
                valores.insert(i, valor)
                print(f'valor {valor} na {i}ª posição da lista...')
                break
print('-='*40)
print(f'Os valores digitados em ordem crescente foram: {valores}')
