
`frase = 'Olá Mundo !'` 

|   O   |   l   |   á   |       |   M   |   u   |   n   |   d   |   o   |       |   !    |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :----: |
| **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** |

`frase.split()`

|       |                 O                  |                 l                  |                 á                  |     |                 M                  |                 u                  |                 n                  |                 d                  |                 o                  |     |                 !                  |       |
| :---: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :-: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :-: | :--------------------------------: | :---: |
|       | <span style="color: yellow;">**0** | <span style="color: yellow;">**1** | <span style="color: yellow;">**2** |     | <span style="color: yellow;">**0** | <span style="color: yellow;">**1** | <span style="color: yellow;">**2** | <span style="color: yellow;">**3** | <span style="color: yellow;">**4** |     | <span style="color: yellow;">**0** |       |
|       | <span style="color: red;">\|-----  |  <span style="color: red;">-----   | <span style="color: red;">-----\|  |     | <span style="color: red;">\|-----  |  <span style="color: red;">-----   |  <span style="color: red;">-----   |  <span style="color: red;">-----   | <span style="color: red;">-----\|  |     | <span style="color: red;">\|----\| |       |
| **[** |                                    |    <span style="color: cyan;">0    |                                    |     |                                    |                                    |    <span style="color: cyan;">1    |                                    |                                    |     |    <span style="color: cyan;">2    | **]** |


`'-'.join(frase.split())`

*Run >*

|                 O                  |                 l                  |                 á                  |   <span style="color: yellow;">-   |                 M                  |                 u                  |                 n                  |                 d                  |                 o                  |   <span style="color: yellow;">-   |                  !                  |
| :--------------------------------: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :--------------------------------: | :---------------------------------: |
| <span style="color: yellow;">**0** | <span style="color: yellow;">**1** | <span style="color: yellow;">**2** | <span style="color: yellow;">**3** | <span style="color: yellow;">**4** | <span style="color: yellow;">**5** | <span style="color: yellow;">**6** | <span style="color: yellow;">**7** | <span style="color: yellow;">**8** | <span style="color: yellow;">**9** | <span style="color: yellow;">**10** |
