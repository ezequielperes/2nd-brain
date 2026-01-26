## Tipos Primitivos
%% O Python Utiliza o str como padrão  %%
Existem 4 tipos de **Tipos Primitivos**:

- **[[int]]**: int vem de *integers* em português, inteiros, eles pegam apenas números inteiros, não funciona números fracionados (1.245, 34.654) lembrando que não pode colocar **ponto**, se colocar o ponto o python entende que você está querendo colocar um número float (número flutuante / Números Reais)
  
  {... ,-3, -2, -1, 0, 1, 2, 3, ...}
  
  Exemplo de utilização:
  
  `valor = int(input('Quantos anos você tem? '))`
  
- **[[float]]**: float vem do *ponto* e/ou *vírgula* dos números fracionados (Reais) eles chamam de "Pontos Flutuantes", funciona tanto números int. quanto os flutuantes, lembrando que **ele só funciona com Ponto ( . )**
  
  {1.2, 59.43, 100.6, 10.0, etc.}
  
  Exemplo De Utilização:
  
  `valor = float(input('Qual foi o valor da compra em R$? '))`

- **[[bool]]:** o bool funciona de uma forma bem interessante, ele utiliza apenas **[[True]]** e **[[False]]** em maiúsculo a primeira letra mesmo, ele vê se algo está vázio ou nn por exemplo:
  
  `nome = bool(input('qual o seu nome? '))`
  
  { True , False }
  
  Se você escrever algo ele vai dar para a variável "nome" = **True**
  Caso contrário, se você não escrever nada ele vai dar para a variável "nome" = **False**
  
  **A variável `nome` não guarda o nome**, guarda `True` ou `False`.
  
- **[[str]]:** str vem de *String* que em português seria linha. Ele funciona com: letras, palavras, textos, e  até números. Entretanto, se colocar números ele vai tratar os números como se fossem textos, e não como números realmente.
  então se você for colocar números no str saiba que você não vai poder fazer cálculos com este número.
  
  {'olá', 'BoM DIa', '7', etc.}
  
  Exemplo De utilização:
  
  `note = str(input('Qual a anotação de hoje? '))`
  
  %% or %%
  
  `note = input('Qual a anotação de hoje? ')`
  
  Lembrando q o **str ele é o padrão** do python, ou seja, apenas colocando input por exemplo o python entende que você está querendo utilizar o str.
  
## Entrada (input) e Saída (print) de Dados

Existem 2 Tipos:

- **[[input]]**: Utilizado para o cliente escrever um valor e dar este valor para uma variável.
  Ele é a **Entrada**
  
  Exemplo De Utilização:
  
  `Nome = input('Qual o seu nome? ')`
  
  %%or%%
  
  `Valor = int(input('Quantas maçãs você tem? '))`
  
  %%or%%
  
  `Pagar = float(input('Qual o valor que está devendo? '))`
  
 `input` **sempre retorna `str`**, e depois você **converte** para `int`, `float`, etc.

- **[[print]]**: Utilizado para escrever uma frase ou um texto ou números, ou até mesmo, valor das variáveis
  Ele é a **Saída**
  
  Exemplo De Utilização:
  
  `print('Olá mundo!')`
  
  %%or%%
  
  `s = 5`
  `print('O valor de s é:' , s)`
  
  %%or%%
  
  `s = 5`
  `print('O valor de s é: {}'.format(s))`
  
  %%or%%
  **O jeito mais certo atualmente:
    `s = 5`
    `print(f'O valor de s é: {s}')`
  
  Percebe-se que tem várias formas de se utilizar o **print** temos como escrever apenas uma frase, colocar frase com as variáveis, e de várias formas, hoje em dia é mais utilizado para a formatação de variáveis o .[[format]] e o [[f-string]] que também é muito utilizado
## Extra: x.is

[[is]] é um método utilizado para dar um valor **[[True]]** ou **[[False]]** para textos, por exemplo X é a nossa variável, vamos supor:

x = 7

print(x.isnumeric())

neste caso ele daria o valor como **True**

x = olá

print(x.isnumeric())

neste caso ele daria o valor como **False**

tem vários tipos de .is:

- .isnumeric(): vê se é um número
  
- .isalpha(): vê se é apenas texto
  
- .isalnum() vê se é texto / número
  
- .isdecimal(): vê se é decimal

e tem vários outros tipos, como upper, lower, space, etc.
## Exercícios:

- **DESAFIO 003**
  
  Crie um programa que leia dois números e mostre a soma entre eles.
  
  [[aula 6 ex.03.py]]

- **DESAFIO 004**
  
  Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. 
  
  [[aula 6 ex.04.py]]