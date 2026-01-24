 str vem de *String* que em português seria linha. Ele funciona com: letras, palavras, textos, e  até números. Entretanto, se colocar números ele vai tratar os números como se fossem textos, e não como números realmente.
  então se você for colocar números no str saiba que você não vai poder fazer cálculos com este número.
  
  {'olá', 'BoM DIa', '7', etc.}
  
  Exemplo De utilização:
  
  `note = str(input('Qual a anotação de hoje? '))`
  
  %% or %%
  
  `note = input('Qual a anotação de hoje? ')`
  
  Lembrando q o **str ele é o padrão** do python, ou seja, apenas colocando input por exemplo o python entende que você está querendo utilizar o str.
  