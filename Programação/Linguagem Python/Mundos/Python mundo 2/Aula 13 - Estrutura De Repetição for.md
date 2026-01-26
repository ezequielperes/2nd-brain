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
for c in range (0, 11, 2)
		print(c, end=' -> ')
print('Fim')

Run >

0 -> 2 -> 4 -> 6 -> 8 -> 10 -> Fim

- Exercício 46 -> [[aula 13 ex.46.py]]
- Exercício 47 -> [[aula 13 ex.47.py]]
- Exercício 48 -> [[aula 13 ex.48.py]]
- Exercício 49 -> [[aula 13 ex.49.py]]
- Exercício 50 -> [[aula 13 ex.50.py]]
- Exercício 51 -> [[aula 13 ex.51.py]]
- Exercício 52 -> [[aula 13 ex.52.py]]
- Exercício 53 -> [[aula 13 ex.53.py]]
- Exercício 54 -> [[aula 13 ex.54.py]]
- Exercício 55 -> [[aula 13 ex.55.py]]
- Exercício 56 -> [[aula 13 ex.56.py]]
- Exercício GPT13 -> [[aula 13 ex.gpt13.py]]
- Exercício GPT14 -> [[aula 13 ex.gpt14.py]]

