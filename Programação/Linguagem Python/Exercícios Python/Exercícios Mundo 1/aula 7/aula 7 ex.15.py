dia = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quanto Km foi rodado?'))
print(f'Você andou {dia} e rodou {km:.2f}km, o valor a ser pago é de: R${(dia*60+km*0.15):.2f}')
