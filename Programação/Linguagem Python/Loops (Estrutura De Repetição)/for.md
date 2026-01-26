O [[for]] ele é uma: 

- Estrutura de repetição
- Laço
- Loop

Pode ser chamado dessas 3 formas, ele cria uma repetição, com 3 parâmetros

`for c in `[[range]]` (x, y, z)`

traduzindo, seria para c num intervalo de (x, y, z)

- c -> contador/índice
- x -> início
- y -> fim
- z -> (passo) pode ser:
	positivo → cresce
	negativo → decresce
	
	Mas **ir ao contrário** só funciona se:
	
	início > fim
    
	passo negativo

Exemplos:
`for c in range (0, 10, 1)`
	`print(c, `[[end]]`=' -> ')`
`print('Fim')`

Run >

0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> Fim

Percebe-se q ele não considera o ultimo número, no caso o 10, no caso, se fosse para aparecer o 10 seria:

`for c in range (0, 11, 2)
	`print(c, end=' -> ')
`print('Fim')`

Run >

0 -> 2 -> 4 -> 6 -> 8 -> 10 -> Fim

