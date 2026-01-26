
O range é uma função usada **principalmente junto com o `for`**, para definir **quantas vezes o laço vai se repetir** e **como essa contagem acontece**.

Ele gera uma **sequência de números** dentro de um **intervalo**.

---

### Estrutura

`range(x, y, z)`

Onde:

- `x` → início da contagem (**inclusivo**)

- `y` → fim da contagem (**não é incluído**)

- `z` → passo (de quanto em quanto a contagem anda)

O `range` pode ter **1, 2 ou 3 parâmetros**.

---

### Formas de uso

`range(10)`

- Começa em `0`
    
- Vai até `9`
    

`range(2, 6)`

- Começa em `2`
    
- Vai até `5`
    

`range(0, 11, 2)`

- Começa em `0`
    
- Vai até `10`
    
- Pulando de `2` em `2`
    

---

### Exemplo prático

`for c in range(0, 5):
	`print(c)`

Saída:

`0 1 2 3 4`

👉 O número `5` **não aparece**, pois o `range` **não inclui o valor final**.

---

### Contagem ao contrário

Para contar de trás pra frente:

- o início deve ser maior que o fim
    
- o passo deve ser negativo
    

`for c in range(10, 0, -1):     print(c)`

Saída:

`10 9 8 7 6 5 4 3 2 1`

---

### Observações importantes

- O `range` **não cria uma lista**, ele gera os valores conforme o laço precisa
    
- É muito usado para:
    
    - contadores
        
    - repetições
        
    - percorrer intervalos numéricos