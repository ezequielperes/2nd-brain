O [[while]] é uma Estrutura de repetição/loop, como o for, entretanto diferente do for. o while ele não tem um intervalo de parada, ele tem uma condição. O while é ideal quando não sabemos previamente quantas vezes o código vai se repetir pois depende de uma [[condição]] lógica:

Exemplo:

`resposta = ' '`
`soma = 0`
`c = 0`
`while resposta not in 'N':`
	`n = int(input('Digite um valor para soma-los: '))`
		`soma += n`
		`c += 1`
	`resposta = input('Você deseja continuar ?').strip().upper()[0]`
		`while resposta not in 'SN'`
			`print('\033[31mResposta Inválida... Digite novamente!\033[m')`
			`resposta = input('Deseja continuar? ').strip().upper()[0]`
`print(f'A soma dos {c} números digitados foi de: {soma})`

Run >

Digite um valor para soma-los: <span style="color: lime;">5</span>
Você deseja continuar ?<span style="color: lime;">x</span>
<span style="color: red;">Resposta Inválida... Digite novamente!</span>
Deseja continuar? <span style="color: lime;">h</span>
<span style="color: red;">Resposta Inválida... Digite novamente!</span>
Deseja continuar? <span style="color: lime;">sa</span>
Digite um valor para soma-los: <span style="color: lime;">10</span>
Você deseja continuar?<span style="color: lime;">nãow</span>
A soma dos 2 números digitados foi de: 15

Percebe-se que o primeiro loop while está dizendo o seguinte:

`while resposta not in 'N': `

Enquanto Resposta não estiver em 'N':

Ou seja, enquanto a variável resposta não condizer com N, o loop vai continuar, até a variável resposta receber N. Poderia ter escrito de outra forma também

`while resposta != 'N':`

Desta forma ele daria no mesmo resultado

O segundo loop, ele faz uma correção, caso o usuário que estiver usando errado a letra, enquanto a variável resposta não receber um valor que estiver em SN ele não vai sair do loop.

Vale ressaltar que quando o loop while não for utilizado corretamente, o while pode entrar em um loop infinito.