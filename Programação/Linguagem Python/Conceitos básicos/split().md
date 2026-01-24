
`frase = 'Olá Mundo !'` 

|   O   |   l   |   á   |       |   M   |   u   |   n   |   d   |   o   |       |   !    |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :----: |
| **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** |

`frase.split()`

*Run* >

|       |                 O                  |                 l                  |                 á                  |     |                 M                  |                 u                  |                 n                  |                 d                  |                 o                  |     |                 !                  |       |
| :---: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :-: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :-: | :--------------------------------: | :---: |
|       | <span style="color: yellow;">**0** | <span style="color: yellow;">**1** | <span style="color: yellow;">**2** |     | <span style="color: yellow;">**0** | <span style="color: yellow;">**1** | <span style="color: yellow;">**2** | <span style="color: yellow;">**3** | <span style="color: yellow;">**4** |     | <span style="color: yellow;">**0** |       |
|       | <span style="color: red;">\|-----  |  <span style="color: red;">-----   | <span style="color: red;">-----\|  |     | <span style="color: red;">\|-----  |  <span style="color: red;">-----   |  <span style="color: red;">-----   |  <span style="color: red;">-----   | <span style="color: red;">-----\|  |     | <span style="color: red;">\|----\| |       |
| **[** |                                    |    <span style="color: cyan;">0    |                                    |     |                                    |                                    |    <span style="color: cyan;">1    |                                    |                                    |     |    <span style="color: cyan;">2    | **]** |

**Exemplo melhor!**
`frase = 'Olá Mundo!'`

`dividido = frase.split()`

`print(dividido[0])`

*Run >*

Olá

%%or%%

`frase = 'Olá Mundo!'`

`dividido = frase.split()`

`print(dividido[1][0:4])`

*Run >*

Mund
