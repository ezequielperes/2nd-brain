def leiadinheiro(txt):
    while True:
        valor = input(txt).strip().replace(',','.')
        if valor.isalpha() or valor == '':
            print(f'\033[31mERRO: "{valor}" é um preço inválido.\033[m"')
        else:
            valor = float(valor)
            break
    return valor

