Existem vários tipos de Operadores Aritméticos no Python, entretanto, Os operadores básicos são:

## Operadores Básicos:

- ( + ): [[Adição]]
  
  Exemplo De Utilização:
  
  5 + 2 == 7
  
- ( - ): [[Subtração]]
  
  Exemplo De Utilização:
  
  5 - 2 == 3

- ( * ): [[Multiplicação]]
  
  Exemplo De Utilização:
  
  5 * 2 == 10
  
- ( / ): [[Divisão]]
  
  Exemplo De Utilização:
  
  5 / 2 == 2.5
  
  Ele vai dar apenas números flutuantes 
  
  4 / 2 == 2.0
  
- ( ** ): [[Potência]]
  
  Exemplo De Utilização:
  
  5 ** 2 == 25
  (Potência)
  
  %%or%%
  
  4 ** (1/2) == 2
  (Raiz Quadrada)
  
  %%or%%
  
  125 ** (1/3) == 5
  (Raiz Cúbica)
  
- ( // ): [[Divisão Inteira]]
  
  5 // 2 == 2
  
  5   <u>|2</u>
  4   2 -> ==Divisão Inteira==
  -
  1 -> Resto da divisão
  
  Ele pega apenas a Divisão inteira, a parte depois do ponto flutuante é descartada
  
- ( % ): [[Resto Da Divisão]]
  
  5 % 2 == 1
  
  Ele pega o resto da Divisão inteira, por exemplo:
  
  5   <u>|2</u>
  4   2 -> Divisão Inteira
  -
  1 -> ==Resto da divisão
  ==

## [[Ordem De Precedência]]

- 1° -> Parênteses ()
- 2° -> [[Potência]] ( ** )
- 3° -> [[Multiplicação]] ( * ), [[Divisão]] ( / ), [[Divisão Inteira]] ( // ) e [[Resto Da Divisão]] (%)

Exemplo De Utilização

2 + 4 ** 2 * 4 + (4 - 2) = 68

Temos que fazer:

1° -> (4 - 2) == 2
2° -> 4 ** 2 == 16
3° -> 16 * 4 == 64
4° -> 2 + 64 + 2 == $68$

## [[Operadores Básicos em Strings]]

Também dá pra se utilizar em textos os operadores básicos

- `+` em texto → concatenação
    
- `*` em texto → repetição
    
- `-`, `/`, `//`, `%`, `**` → **NÃO** funcionam com [[str]] (strings)

Exemplos de Utilização:

----

'Oi' + 'Olá'

Run >

'OiOlá'

----

'Oi' * 3

Run >

'OiOiOi'

---

print ('=' * 20)

Run >

====================

---

## [[Alinhamentos]]

Utilizado para alinhar um item para um tanto de caracteres

- Alinhamentos funcionam apenas em [[f-string]] ou [[format]]

Exemplo De Utilização:

---

nome = input('Qual é o seu nome? ')

print(f'Prazer em te conhecer {nome==:20==} !')

Run >

Qual é o seu nome? <span style="color: red;">Ezequiel</span>
`Prazer em te conhecer Ezequiel             !`
                        20 caracteres
                        Incluindo Ezequiel

---

%%Or%% 

print(f'Prazer em te conhecer {nome==:>20==} !')

Run >

`Prazer em te conhecer             Ezequiel !`
                        20 caracteres
                        Incluindo Ezequiel

---

%%Or%%

print(f'Prazer em te conhecer {nome==:^20==} !')

Run >

`Prazer em te conhecer       Ezequiel       !`
                        20 caracteres
                        Incluindo Ezequiel

---

%%Or%%

print(f'Prazer em te conhecer {nome==:=^20==} !')

Run >

`Prazer em te conhecer ======Ezequiel====== !`
                        20 caracteres
                        Incluindo Ezequiel

## Exercícios

- Exercício 05 - Antecessor e Sucessor
  
  [[aula 7 ex.05.py]]
  
  Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

- Exercício 06 - Dobro, Triplo, Raiz Quadrada
  
  [[aula 7 ex.06.py]]
  
  Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

- Exercício 07 - média Aritmética
  
  [[aula 7 ex.07.py]]
  
  Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média

- Exercício 08 - Conversor de Medidas
  
  [[aula 7 ex.08.py]]
  
  Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros

- Exercício 09 - Tabuada
  
  [[aula 7 ex.09.py]]
  
  Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

- Exercício 10 - Conversor De Moedas
  
  [[aula 7 ex.10.py]]
  
  Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar 
  **Considere
  US$ 1,00 = R$3,27**

- Exercício 11 - Pintando Parede
  
  [[aula 7 ex.11.py]]
  
  Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

- Exercício 12 - Calculando Descontos
  
  [[aula 7 ex.12.py]]
  
  Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

- Exercício 13 - Reajuste Salarial 
  
  [[aula 7 ex.13.py]]
  
  Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

- Exercício 14 - Conversor de Temperaturas
  
  [[aula 7 ex.14.py]]
  
  Escreva um programa que converta uma temperatura digitada em °C e converta para °F

- Exercício 15 - Aluguel de Carros
  
  [[aula 7 ex.15.py]]
  
  Escreva um programa que pergunte a quantidade de Km percorridos de um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado

- Exercício 01GPT - 
  
  **Sem rodar o código**, diga qual será o resultado final:

`resultado = 10 + 3 * 2 ** 2 - (6 // 4) print(resultado)`

👉 Resolva **passo a passo**, seguindo a **ordem de precedência**.

==resultado = 21==
  
- Exercício 02GPT -
  Escreva um código que:

1. Peça o nome do usuário
    
2. Mostre o nome **centralizado em 20 caracteres**
    
3. Use `-` como preenchimento
    
4. Imprima uma linha com `=` repetido 30 vezes
    

### Exemplo de saída (nome = Ana):

`=============== ------Ana------- ===============`

_(os espaços contam, o nome também)_

[[aula 7 gpt.02.py]
]


