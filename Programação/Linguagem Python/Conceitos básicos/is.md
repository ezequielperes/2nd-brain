
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