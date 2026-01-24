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