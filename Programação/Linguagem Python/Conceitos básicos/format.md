`.format()` é um **método de string** usado para **substituir partes de um texto por valores de variáveis**.

Ou seja:  
você escreve um texto com **espaços reservados `{}`** e depois diz ao Python **quais valores entram nesses lugares**.

Exemplo:

`nome = 'Ezequiel' idade = 18  print('Meu nome é {} e eu tenho {} anos'.format(nome, idade))`

O Python pega os valores de `nome` e `idade` e coloca dentro das `{}`.

Resumindo:  
**`.format()` serve para montar textos dinâmicos usando variáveis.**