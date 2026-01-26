Temos duas formas de parar o [[while]]:

- Quando a **condição** do `while` se torna [[False]]
    
- Ou utilizando a instrução [[break]]
    

O [[break]] é utilizado para **interromper imediatamente** a execução do loop, **independente da condição** definida no `while`.

Quando o `break` é executado, o Python **sai do loop na hora** e continua o programa **a partir da próxima linha fora do loop**.

O `break` é muito usado quando:

- Encontramos um valor específico
    
- O usuário digita algo que indica parada
    
- Uma condição interna torna desnecessário continuar o loop
    

Exemplo:

`while `[[True]]`:
	`n = int(input('Digite um número: '))`     
	`if n == 0:`        
		`break`
	`print(f'Você digitou {n}')`
`print('Loop finalizado')`

Nesse exemplo:

- O [[while]] [[True]] criaria um loop infinito
    
- O `break` é responsável por **encerrar o loop** quando o usuário digita `0`
    

Ou seja, mesmo que a condição do `while` seja sempre verdadeira (`True`), o `break` força a saída do loop.
O break interrompe imediatamente o loop mais próximo em que ele está, ignorando a condição do while.

- Exercício 66 -> [[aula 15 ex.66.py]]
- Exercício 67 -> [[aula 15 ex.67.py]]
- Exercício 68 -> [[aula 15 ex.68.py]]
- Exercício 69 -> [[aula 15 ex.69.py]]
- Exercício 70 -> [[aula 15 ex.70.py]]
- Exercício 71 -> [[aula 15 ex.71.py]]
- Exercício GPT17 -> [[aula 15 ex.gpt17.py]]
- Exercício GPT18 -> [[aula 15 ex.gpt18.py]]