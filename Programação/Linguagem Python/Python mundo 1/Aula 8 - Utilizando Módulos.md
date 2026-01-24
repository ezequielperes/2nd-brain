Os [[módulos]] são **bibliotecas (módulos) que adicionam funcionalidades** à linguagem de programação, e no **Python** não seria diferente.

Existem diversos tipos de módulos, como o [[math]] e o statistics, que servem para operações matemáticas mais avançadas, como:

- [[sqrt]] (função do módulo [[math]])
    
- randint (função do módulo random)
    

Entretanto, os módulos **não servem apenas para matemática**. Existem módulos voltados para diferentes finalidades, como sistema operacional, tempo, interface gráfica, dados e muito mais.

## Classificação dos módulos para nível iniciante

### Iniciante

- [[math]] — matemática mais avançada que o padrão do Python

- [[random]] — geração de números e escolhas aleatórias

- [[time]] — controle de tempo e pausas

- [[datetime]] — datas e horários

- [[emoji]] — permite o uso de emojis no programa

## Como se utilizam os módulos?

Para utilizar a biblioteca de um certo módulo, basta:

[[import]] (nome do módulo)

ou se você quer pegar alguma função do módulo, basta:

[[from]] (nome do módulo) [[import]] (nome da função do módulo)

por exemplo, se eu quero utilizar toda a biblioteca de algum módulo, o certo a se fazer é:

`import math`

neste caso todas as funções e objetos do módulo math vai ser importada pro programa

**Boa Prática!: sempre que for usar [[import]] ou [[from]] sempre deixar eles na primeira linha do programa**

Caso eu queira utilizar apenas uma função do módulo, o certo a se fazer é:

`from math import sqrt`

Caso você queira utilizar mais de uma função do módulo, o certo a se fazer é:

`from math import sqrt, sin, cos, tan`

**<span style="color: red;">Lembre-se: Funções são blocos de código que executam uma tarefa específica.**  
**Quando pertencem a um módulo, são chamadas de funções do módulo. </span>** 


## Exercícios:

- Exercício 16 -> [[aula 8 ex.16.py]]

- Exercício 17 -> [[aula 8 ex.17.py]]

- Exercício 18 -> [[aula 8 ex.18.py]]

- Exercício 19 -> [[aula 8 ex.19.py]]

- Exercício 20 -> [[aula 8 ex.20.py]]

- Exercício 21 -> [[aula 8 ex.21.py]] and [[aula 8 ex.21.mp3]]
  
  Exercício GPT03 -> [[aula 8 ex.gpt03.py]]
  
  Exercício GPT04 -> [[aula 8 ex.gpt04.py]]
  