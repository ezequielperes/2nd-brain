celsius = float(input('Qual a temperatura em celsius? '))
print(f'A temperatura de {celsius:.2f}°C corresponde a:\n'
f'{(celsius*1.8+32):.2f}°F (fahrenheit)\n '
      f'E {(celsius+273):.2f}K (Kelvin)')