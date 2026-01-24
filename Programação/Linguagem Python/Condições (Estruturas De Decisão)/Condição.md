## [[Condição]]
As **condições** permitem que o programa **tome decisões** com base em comparações lógicas.

[[If]]: -> verifica uma condição
<span style="color: lime;">Bloco</span> [[True]] (executa se a condição for verdadeira)

[[Else]]: -> executa caso a condição seja falsa
<span style="color: red;">Bloco</span> [[False]] (Executa se a condição for falsa)

## Operadores De Comparação

[[Maior]] -> ( > )

[[Menor]] -> ( < )

[[Maior-Igual]] -> ( >= )

[[Menor-Igual]] -> (<=)

[[Igual]] -> ( == )

[[Diferente De]] -> ( != )

Exemplo De Utilização:

``if idade >= 18:
`print('Maior de 18 anos')`
## Operadores lógicos

São usados para **combinar condições**.
### [[and]]

Todas as condições precisam ser verdadeiras

[[if]] idade >= 18 [[and]] idade <= 65
    print('Idade válida')`

### [[or]]

Basta **uma condição** ser verdadeira

[[if]] dia == 'sábado' [[or]] dia == 'domingo':
    print('Fim de semana')

### [[not]]

Inverte o resultado da condição

[[if]] [[not]] idade >=18:
    print('Menor de 18 anos')

## Exercícios

